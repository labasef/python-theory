# Libraries and Modules

Modules and libraries are fundamental to Python's code organization and reusability. They allow you to organize code into manageable, reusable components.

## Modules

A module is a Python file (`.py`) containing definitions and statements. It serves as a logical way to organize related code.

### Creating a Module
```python
# math_operations.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

### Using a Module
```python
import math_operations
result = math_operations.add(5, 3)  # Returns 8
```

## Libraries (Packages)

A library (or package) is a collection of modules organized in a directory hierarchy. It contains an `__init__.py` file that marks it as a package.

### Package Structure
```
my_library/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

### Importing from Packages
```python
from my_library import module1
from my_library.subpackage import module3
from my_library.module1 import some_function
```

## Standard Library

Python comes with a comprehensive standard library including:
- **os**: Operating system interfaces
- **sys**: System-specific parameters and functions
- **math**: Mathematical functions
- **datetime**: Date and time handling
- **json**: JSON encoding and decoding
- **re**: Regular expressions
- **collections**: Specialized data structures
- **itertools**: Iteration tools

## Third-party Libraries

Popular third-party libraries extend Python's capabilities:
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Requests**: HTTP library
- **Django/Flask**: Web frameworks
- **TensorFlow/PyTorch**: Machine learning

## Best Practices

1. **Organize code logically** into modules and packages
2. **Use meaningful names** for modules and functions
3. **Document your code** with docstrings
4. **Avoid circular imports** by planning module dependencies
5. **Use virtual environments** to manage project dependencies

