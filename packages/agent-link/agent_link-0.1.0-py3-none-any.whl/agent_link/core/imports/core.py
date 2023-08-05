import os
import inspect
import importlib
import sys
from types import FunctionType

def export_all_functions(path):
    current_folder = os.path.abspath(path)
    sys.path.insert(0, current_folder)
    
    function_list = []

    for root, dirs, files in os.walk(current_folder):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, current_folder)
                module_name = rel_path.replace(os.sep, ".")[:-3]
                
                try:
                    module = importlib.import_module(module_name)

                    # Add all functions in the module to the function_list
                    for name, obj in vars(module).items():
                        if isinstance(obj, FunctionType):
                            function_list.append((module_name, name))

                except Exception as e:
                    print(f"Error importing '{module_name}':\n{e}")

    sys.path.pop(0)

    return function_list