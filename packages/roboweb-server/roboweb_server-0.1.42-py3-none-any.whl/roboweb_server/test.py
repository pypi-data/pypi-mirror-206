import ast
import astunparse  # Import the astunparse module
import inspect
import json
import warnings
from tqdm import TqdmExperimentalWarning

# Filter out the TqdmExperimentalWarning
warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)

requestJson = """
{"notebook":{"metadata":{"kernelspec":{"display_name":"Python 3 (ipykernel)","language":"python","name":"python3"},"language_info":{"codemirror_mode":{"name":"ipython","version":3},"file_extension":".py","mimetype":"text/x-python","name":"python","nbconvert_exporter":"python","pygments_lexer":"ipython3","version":"3.11.2"}},"nbformat_minor":5,"nbformat":4,"cells":[{"cell_type":"code","source":"hello","metadata":{"trusted":true,"tags":[]},"execution_count":1,"outputs":[{"ename":"NameError","evalue":"name 'hello' is not defined","output_type":"error","traceback":["\\u001b[0;31m---------------------------------------------------------------------------\\u001b[0m","\\u001b[0;31mNameError\\u001b[0m                                 Traceback (most recent call last)","Cell \\u001b[0;32mIn[1], line 1\\u001b[0m\\n\\u001b[0;32m----> 1\\u001b[0m \\u001b[43mhello\\u001b[49m\\n","\\u001b[0;31mNameError\\u001b[0m: name 'hello' is not defined"]}],"id":"2653e868-4bd9-4f53-bc55-2da4bdfefa4b"},{"cell_type":"code","source":"","metadata":{"trusted":true},"execution_count":null,"outputs":[],"id":"92ffc4e4-2029-4563-9936-cf28357596c6"}]},"userToken":"hello","userPrompt":[1]}
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
    print(json.dumps(request, indent=2))
    # Sample code for testing
    # analyze_code(notebook)