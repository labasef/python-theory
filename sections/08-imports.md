# Imports

Imports allow you to use code from other modules and packages in your Python program. Understanding how to properly import and organize imports is crucial for writing clean, maintainable code.

## Basic Import Statements

### Import Entire Module
```python
import math
print(math.pi)
print(math.sqrt(16))
```

### Import Specific Names
```python
from math import pi, sqrt
print(pi)
print(sqrt(16))
```

### Import with Alias
```python
import numpy as np
from datetime import datetime as dt

array = np.array([1, 2, 3])
now = dt.now()
```

### Import All Names (use with caution)
```python
from math import *
print(pi)  # Works, but can cause namespace pollution
```

## Module Search Path

When you import a module, Python searches in this order:
1. Built-in modules
2. Directories in `sys.path` (which includes the current directory)
3. `PYTHONPATH` environment variable
4. Installation-dependent default paths

### Viewing Module Path
```python
import sys
print(sys.path)  # List of directories Python searches
```

## Types of Imports

### Absolute Imports
Importing from the top level of your package hierarchy:
```python
from mypackage.subpackage import module
from mypackage.module import function
```

### Relative Imports
Importing relative to the current module (within packages):
```python
# In mypackage/subpackage/module.py
from . import sibling_module        # Same package
from .. import parent_module        # Parent package
from ..sibling_package import other # Sibling package
```

## Import Best Practices

### 1. Import Order
Follow PEP 8 conventions:
```python
# Standard library imports
import os
import sys
from datetime import datetime

# Third-party imports
import numpy as np
import pandas as pd

# Local application imports
from myapp.models import User
from myapp.utils import helper
```

### 2. Avoid Circular Imports
```python
# module_a.py
from module_b import function_b  # Circular!

# module_b.py
from module_a import function_a  # Circular!

# Solution: Reorganize or use late imports
```

### 3. Use Absolute Imports
Prefer absolute imports for clarity:
```python
# Good
from myproject.utils import helper

# Avoid (relative, less clear)
from ..utils import helper
```

### 4. Import Only What You Need
```python
# Good - specific imports
from os.path import join, exists

# Less ideal - imports entire module
import os.path
```

## The `__name__` Variable

Used to determine if a module is being run directly or imported:

```python
if __name__ == "__main__":
    # Code here runs only when script is executed directly
    # Not run when module is imported
    print("Running as main script")
else:
    print("Module was imported")
```

## Common Standard Library Imports

```python
import os                    # Operating system interface
import sys                   # System-specific parameters
import math                  # Mathematical functions
import json                  # JSON encoding/decoding
import re                    # Regular expressions
import datetime              # Date and time
import random                # Random number generation
import collections           # Specialized data structures
from pathlib import Path     # Object-oriented filesystem paths
```

## Troubleshooting Imports

### ModuleNotFoundError
- Module doesn't exist or wrong name
- Module not installed
- Not in Python path

### ImportError
- Module exists but import statement is wrong
- Circular import issue
- Module has errors preventing import

### Solution Tips
```python
# Add directory to path
import sys
sys.path.append('/path/to/directory')

# Check if module is installed
import importlib.util
spec = importlib.util.find_spec("module_name")
is_installed = spec is not None
```

