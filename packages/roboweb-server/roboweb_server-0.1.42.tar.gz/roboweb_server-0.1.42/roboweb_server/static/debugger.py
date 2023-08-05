import warnings
from tqdm import TqdmExperimentalWarning
warnings.filterwarnings('ignore')

import sys
import inspect
import re
from ipykernel.comm import Comm
from IPython.core import ultratb

class TypeErrorHandler(object): 
    
    # TypeError: create_index() got an unexpected keyword argument 'index_name'
    def handle(self, exception_line, exc_type, exc_value, tb):
        error_message = exc_value.args[0]
        pattern = r"(.+)\(\) got an unexpected keyword argument '(.+)'"
        
        match = re.match(pattern, error_message)
        if not match:
            return
        
        attribute_name = match.group(1)
        argument_name = match.group(2)
        
        pattern = r"(.+).{0}.+".format(attribute_name)
        match = re.match(pattern, exception_line)
        module_name = match.group(1)
        module_object = sys.modules[module_name]
        
        # find docstring of function module_name.attribute_name
        module_functions = inspect.getmembers(module_object, inspect.isfunction)
        for function_name, function_object in module_functions:
            if function_name == attribute_name:
                docstring = inspect.getdoc(function_object)
                break
                
        return f"""
The function {attribute_name} does not have the argument {argument_name}.

These are the arguments of the function:
    
{docstring}
        """

class FunctionSummary(object): 
    def __init__(self, function_name, function_object):
        self.function_name = function_name
        self.signature = inspect.signature(function_object)
        self.docstring = inspect.getdoc(function_object)
        
    def short_summary(self) -> str:
        return f"{self.function_name}{self.signature}"
    
    def long_summary(self):        
        return f"{self.function_name}{self.signature}\n {self.docstring}"
class ClassSummary(object):
    def __init__(self, class_name, class_object):
        self.class_name = class_name
        self.docstring = inspect.getdoc(class_object)
    
    def short_summary(self) -> str:
        return f"{self.class_name}\n {self.docstring}" 
    def long_summary(self) -> str:
        return f"{self.class_name}\n {self.docstring}"
    
class ModuleSummary(object):
    def __init__(self, module_object): 
        self.module_functions = inspect.getmembers(module_object, inspect.isfunction)
        self.module_classes = inspect.getmembers(module_object, inspect.isclass)

        
    def function_summary(self) -> str:
        return "\n".join([FunctionSummary(function_name, function_obj).short_summary() for (function_name, function_obj) in self.module_functions])
    
    def class_summary(self) -> str:
        return "\n\n".join([ClassSummary(class_name, class_obj).short_summary() for (class_name, class_obj) in self.module_classes])    
 
class AttributeErrorHandler(object):
    
    def handle_module(self, error_message):
        pattern = r"module '(.+)' has no attribute '(.+)'"

        match = re.match(pattern, error_message)
        if not match:
            return
         
        module_name = match.group(1)
        attribute_name = match.group(2)
        module_object = sys.modules[module_name]

        # if attribute_name starts with caps then it is a class
        module_summary = ModuleSummary(module_object)
        if attribute_name[0].isupper():
            return f"""
These are the only classes in the {module_name} module:

{module_summary.class_summary()}
            """
        else:             
            return f"""
Do not use the {attribute_name}() function.
These are the only functions in {module_name} module:

{module_summary.function_summary()}
            """
    
    def handle_class(self, error_message):
        pattern = r"'(.+)' object has no attribute '(.+)'"
        match = re.match(pattern, error_message)

        if not match:
            return
         
        class_name = match.group(1)
        attribute_name = match.group(2)
        class_object = sys.modules[class_name]
        class_methods = inspect.getmembers(class_name, inspect.isfunction)
                
        return f"""
These are the only methods in {class_name}
        
{class_methods}
        """
    
    def handle(self, exception_line, exc_type, exc_value, tb):
        error_message = exc_value.args[0]
        if self.handle_module(error_message):
            return self.handle_module(error_message)
        elif self.handle_class(error_message):
            return self.handle_class(error_message)
        else:
            return "" 
        
        
def exception_handler(self, etype, evalue, etb, tb_offset=None):
    # Create an instance of the IPython VerboseTB formatter
    formatter = ultratb.VerboseTB()

    # Print the formatted traceback information along with the exception message
    print(formatter.text(etype, evalue, etb))

    # Walk the traceback to find the frame where the exception was raised
    frames = inspect.getinnerframes(etb)
    last_frame = frames[-1].frame
    context = generate_context(last_frame, etype, evalue, etb) 
    comm.send(context)
    
    del last_frame
        
def get_local_vars(frame): 
    # Get the local variables from the frame
    local_vars = frame.f_locals.items()
    
    # Print the local variables
    if len(local_vars) > 0:
        print("\nLocal variables at the time of the exception:")
        for name, value in local_vars:
            print(f"{name} = {value}")
    
def generate_context(frame, exc_type, exc_value, exc_tb):
    # co = frame.f_code
    frame_info = inspect.getframeinfo(frame)
    exception_line = frame_info.code_context[0].strip()
    exception_name = exc_type.__name__
    exception_message = str(exc_value)      

    module_name = frame.f_globals.get('__name__')
    if exc_type is AttributeError:
        handler_type = "AttributeError Debugger"
        handler_message = AttributeErrorHandler().handle(exception_line, exc_type, exc_value, exc_tb)
    elif exc_type is TypeError:
        handler_type = "TypeError Debugger"
        handler_message = TypeErrorHandler().handle(exception_line, exc_type, exc_value, exc_tb)
    else:
        handler_type = "Debugger"
        handler_message = ""
        
    return {'context': handler_message, 'type': handler_type}
 
    
comm = Comm(target_name='debugger_comm_target')
ip = get_ipython()
ip.set_custom_exc((Exception,), exception_handler)
