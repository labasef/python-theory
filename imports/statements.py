import math
import sys
import os

# the sys.path list contains the directories that Python will search for modules
print(sys.path)

# the os.environ dictionary contains the environment variables
print(os.environ.get('PYTHONPATH', 'not found'))

# The sys.modules dictionary contains all the modules that have been imported
print(sys.modules.get('math', 'not found'))

# list the contents of the math namespace
print(dir(math))

print(globals())

# The math module is an object
print(math.pi)

# import the custom module my_module
import my_module

print(dir(my_module))
my_module.my_function()

import importlib

# reload the module my_module
importlib.reload(my_module)


