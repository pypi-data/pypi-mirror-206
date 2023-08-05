import ast
import astunparse  # Import the astunparse module
import inspect
import json
import warnings
from tqdm import TqdmExperimentalWarning

# Filter out the TqdmExperimentalWarning
warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)

requestJson = """
{{requestJson}}
"""


def analyze_code(code):
    # Parse the code using the ast module
    tree = ast.parse(code)

    # Define a custom AST visitor to collect function signatures and calls
    class FunctionInfoCollector(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            # Collect the argument names and types for the function
            arg_info = [(arg.arg, astunparse.unparse(arg.annotation).strip(), arg.default is None) for arg in node.args.args]
            function_signatures[node.name] = arg_info
            # Collect the docstring for the function
            function_docstrings[node.name] = ast.get_docstring(node)
            self.generic_visit(node)

        def visit_Call(self, node):
            # Collect function call information
            if hasattr(node.func, 'id'):
                function_name = node.func.id
                function_calls[function_name] = node
            self.generic_visit(node)

        def visit_Import(self, node):
            # Collect imported modules
            for alias in node.names:
                imported_modules.append(alias.name)
            self.generic_visit(node)

        def visit_ImportFrom(self, node):
            # Collect imported modules
            imported_modules.append(node.module)
            self.generic_visit(node)

    # Use the custom AST visitor to collect function signatures, calls, and docstrings
    function_signatures = {}
    function_docstrings = {}
    function_calls = {}
    imported_modules = []
    collector = FunctionInfoCollector()
    collector.visit(tree)

    # Load imported modules and retrieve their function signatures
    module_info = {}
    for module_name in imported_modules:
        try:
            module = __import__(module_name)
            functions = {}
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                try:
                    signature = [(param_name, param.annotation.__name__ if param.annotation != inspect.Parameter.empty else "", "required" if param.default is inspect.Parameter.empty else "") for param_name, param in inspect.signature(obj).parameters.items()]
                    docstring = inspect.getdoc(obj)
                    functions[name] = {
                        "signature": signature,
                        "docstring": docstring
                    }
                except ValueError:
                    # Skip functions for which a signature cannot be retrieved
                    pass
            module_info[module_name] = functions
        except ImportError:
            print(f"Warning: Unable to import module '{module_name}'.")

    # Convert the module information to a JSON array
    json_output = json.dumps(module_info, indent=4)

    # Print the JSON array
    print(json_output)
    

if __name__ == '__main__':
    request = json.loads(requestJson)
    print(json.dumps("hello world"))
    # print(json.dumps(request))
    # Sample code for testing
    # analyze_code(notebook)
