import arithmetic

print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))

#  we can import module in two ways:

import my_modules.test_module

from my_modules import test_module


#packages
# sample_project
#      |_____ python_file.py
#      |_____ my_modules
#                |_____ __init__.py
#                |_____ test_module.py
#                |_____ another_module.py
#                |_____ third_module.py

# If we create a directory called my_modules, which marks the package name, we can then create a module inside that package called test_module.\

__init__.py
# In Python 3.3+, we only need this file if we need to customize what modules are available to anyone attempting to import the package.
# 
# if we didn't want another_module or third_module to be accessible for importing, we could override the __all__ variable, like so:
# sample_project/my_modules/__init__.py
__all__ = ["test_module"]

