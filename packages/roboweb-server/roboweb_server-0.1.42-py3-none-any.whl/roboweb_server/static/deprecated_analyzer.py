import ast
import astunparse
import inspect
import json
import warnings
from tqdm import TqdmExperimentalWarning

# Filter out the TqdmExperimentalWarning
warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)

def analyze_code(code):
    # Parse the code using the ast module
    tree = ast.parse(code)

    # Define a custom AST visitor to collect function definitions, imported modules, and global variable assignments
    class FunctionInfoCollector(ast.NodeVisitor):
        def visit_Import(self, node):
            # Collect imported modules
            for alias in node.names:
                imported_modules.append(alias.name)
            self.generic_visit(node)

        def visit_ImportFrom(self, node):
            # Collect imported modules
            imported_modules.append(node.module)
            self.generic_visit(node)

        def visit_Assign(self, node):
            # Collect global variable assignments
            if isinstance(node.targets[0], ast.Name):
                variable_name = node.targets[0].id
                # Ignore private variables (names starting with an underscore)
                if not variable_name.startswith('_'):
                    global_variables[variable_name] = astunparse.unparse(node.value).strip()
            self.generic_visit(node)

        def visit_FunctionDef(self, node):
            # Collect defined functions and their docstrings
            function_name = node.name
            # Ignore private functions (names starting with an underscore)
            if not function_name.startswith('_'):
                docstring = ast.get_docstring(node) if ast.get_docstring(node) else ""
                summary = docstring.split('\n')[0] if docstring else ""
                defined_functions[function_name] = {
                    "docstring": docstring,
                    "summary": summary
                }
            self.generic_visit(node)

        def visit_ClassDef(self, node):
            # Collect defined classes and their methods
            class_name = node.name
            # Ignore private classes (names starting with an underscore)
            if not class_name.startswith('_'):
                class_methods = {}
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_name = item.name
                        # Ignore private methods (names starting with an underscore)
                        if not method_name.startswith('_') or method_name == "__init__":
                            docstring = ast.get_docstring(item) if ast.get_docstring(item) else ""
                            summary = docstring.split('\n')[0] if docstring else ""
                            class_methods[method_name] = {
                                "docstring": docstring,
                                "summary": summary
                            }
                defined_classes[class_name] = class_methods
            self.generic_visit(node)

    # Use the custom AST visitor to collect defined functions, imported modules, and global variable assignments
    imported_modules = []
    global_variables = {}
    defined_functions = {}
    defined_classes = {}
    collector = FunctionInfoCollector()
    collector.visit(tree)

    # Load imported modules and retrieve their function signatures
    module_info = {}
    for module_name in imported_modules:
        try:
            module = __import__(module_name)
            functions = {}
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                # Ignore private functions (names starting with an underscore)
                if not name.startswith('_'):
                    try:
                        signature = [(param_name, param.annotation.__name__ if hasattr(param.annotation, '__name__') and param.annotation != inspect.Parameter.empty else "", "required" if param.default is inspect.Parameter.empty else "") for param_name, param in inspect.signature(obj).parameters.items()]
                        # create a signature summary by converting into a string 
                        signature_summary = name + "(" + ", ".join([f"[{param_name},{param_type}, {param_default}]" for param_name, param_type, param_default in signature]) + ")"
                        docstring = inspect.getdoc(obj)
                        docstring_summary = docstring.split('\n')[0] if docstring else ""
                        functions[name] = {
                            "signature": signature,
                            "docstring": docstring,
                            "summary": signature_summary + ": " + docstring_summary
                        }
                    except ValueError:
                        # Skip functions for which a signature cannot be retrieved
                        pass

            classes = {}
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # Ignore private classes (names starting with an underscore)
                if not name.startswith('_'):
                    class_methods = {}
                    for method_name, method_obj in inspect.getmembers(obj, inspect.isfunction):
                        # Ignore private methods (names starting with an underscore)
                        if not method_name.startswith('_'):
                            try:
                                signature = [(param_name, param.annotation.__name__ if hasattr(param.annotation, '__name__') and param.annotation != inspect.Parameter.empty else "", "required" if param.default is inspect.Parameter.empty else "") for param_name, param in inspect.signature(method_obj).parameters.items()]
                                # create a signature summary by converting into a string 
                                signature_summary = method_name + "(" + ", ".join([f"[{param_name},{param_type}, {param_default}]" for param_name, param_type, param_default in signature]) + ")"
                                docstring = inspect.getdoc(method_obj)
                                docstring_summary = docstring.split('\n')[0] if docstring else ""
                                class_methods[method_name] = {
                                    "signature": signature,
                                    "docstring": docstring,
                                    "summary": signature_summary + ": " + docstring_summary
                                }
                            except ValueError:
                                # Skip methods for which a signature cannot be retrieved
                                pass
                            
                    summary = ""
                    for _, method_info in class_methods.items():
                        summary += method_info["summary"] + "\n"

                    classes[name] = {
                        'methods' : class_methods,
                        'summary' : summary
                    }

            summary = "\n"
            num = 1
            for _, function_info in functions.items():
                function_summary = function_info["summary"]
                summary += f"{num}. {function_summary} \n"
                num += 1

            module_info[module_name] = {
                'functions': functions,
                'classes': classes,
                'summary': summary

            }

        except ImportError:
            print(f"Warning: Unable to import module '{module_name}'.")

    global_variables_str = '\n'.join([f'{key}={value}' for key, value in global_variables.items()])
    # Convert the module information, global variables, defined functions, and defined classes to a JSON array
    output = {
        "module_info": module_info,
        "global_variables": global_variables_str,
        "defined_functions": defined_functions,
        "defined_classes": defined_classes
    }
    json_output = json.dumps(output, indent=4)
    # json_output = json.dumps(output['module_info']['pinecone']['classes']['Index'], indent=4)

    # Print the JSON array
    print(json_output)
    
    
requestJson = """
{{requestJson}}
"""

if __name__ == '__main__':
    # Sample code for testing
    request = json.loads(requestJson)
    notebook = request["notebook"]
    analyze_code(notebook)
