# Python Interpreter

The Python interpreter is a program that executes Python code. It reads Python code and translates it into machine-executable instructions at runtime.

## How Python Works

### 1. Source Code
You write Python code in `.py` files with readable, human-friendly syntax.

### 2. Parsing
The interpreter reads the source code and parses it into tokens and syntax trees.

### 3. Compilation
The code is compiled into bytecode (`.pyc` files), an intermediate representation that's machine-independent but optimized for the interpreter.

### 4. Execution
The Python Virtual Machine (PVM) executes the bytecode line by line.

## Bytecode

Python compiles source code into bytecode, which:
- Is platform-independent
- Is cached in `__pycache__` directories for faster subsequent imports
- Can be viewed using the `dis` module

### Viewing Bytecode
```python
import dis

def add(a, b):
    return a + b

dis.dis(add)  # Shows the bytecode instructions
```

## Interpreter Modes

### Interactive Mode
Run Python interactively in the shell:
```bash
python
>>> print("Hello, World!")
Hello, World!
```

### Script Mode
Execute a Python script file:
```bash
python script.py
```

## Python Virtual Machine (PVM)

- Executes bytecode instructions
- Manages memory, namespaces, and object references
- Provides runtime services like garbage collection
- Platform-specific (Windows, macOS, Linux implementations)

## Interpreter Implementations

Different implementations of the Python language:
- **CPython**: Reference implementation, written in C (most common)
- **PyPy**: Just-In-Time (JIT) compiler for faster execution
- **Jython**: Runs on the Java Virtual Machine (JVM)
- **IronPython**: Runs on the .NET platform
- **MicroPython**: Lightweight implementation for microcontrollers

## Key Characteristics

1. **Interpreted, not compiled**: No explicit compilation step before running
2. **Dynamic typing**: Type checking happens at runtime
3. **Automatic memory management**: Garbage collection handles cleanup
4. **Bytecode caching**: Compiled code is cached for performance

