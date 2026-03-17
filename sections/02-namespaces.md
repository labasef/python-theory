# Namespaces

A namespace is a mapping from names to objects in Python. It's essentially a dictionary that keeps track of variable names and their associated values.

## Types of Namespaces

### 1. Local Namespace
- Contains local variables defined within a function or method
- Created when a function is called and destroyed when the function returns
- Accessed during function execution

### 2. Enclosing Namespace
- Exists in nested function scenarios
- Contains variables from the enclosing (outer) function
- Used in closures

### 3. Global Namespace
- Contains variables defined at the module level
- Created when a module is imported or script starts
- Accessible throughout the module

### 4. Built-in Namespace
- Contains built-in functions and exceptions (print, len, Exception, etc.)
- Always available to all modules

## Scope and LEGB Rule

Python resolves variable names using the **LEGB** rule:
1. **Local** - Inside the current function
2. **Enclosing** - Inside enclosing functions (nested functions)
3. **Global** - At the module level
4. **Built-in** - In the built-in namespace

When you reference a variable, Python searches in this order until it finds a match.

## Working with Namespaces

### Accessing Global Namespace
```python
print(globals())  # Returns a dictionary of global variables
```

### Accessing Local Namespace
```python
def example():
    local_var = 10
    print(locals())  # Returns a dictionary of local variables
```

### Global and Nonlocal Keywords
```python
global_var = 10

def modify_global():
    global global_var
    global_var = 20  # Modifies the global variable

def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10  # Modifies the variable in the enclosing scope
    inner()
    print(x)  # Prints 10
```

