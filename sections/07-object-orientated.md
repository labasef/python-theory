# Object-Orientated Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects and classes, making code more modular, reusable, and maintainable.

## Core Concepts

### Classes and Objects
- **Class**: A blueprint or template for creating objects
- **Object**: An instance of a class with specific values

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

# Create an object (instance)
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
```

### Attributes and Methods
- **Attributes**: Variables that belong to an object (data)
- **Methods**: Functions that belong to an object (behavior)

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand      # Attribute
        self.model = model      # Attribute
    
    def start(self):            # Method
        return f"{self.brand} {self.model} is starting..."
```

## Four Pillars of OOP

### 1. Encapsulation
Bundling data (attributes) and methods (behavior) together, hiding internal details:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
```

### 2. Inheritance
Creating new classes based on existing ones, promoting code reuse:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### 3. Polymorphism
Objects of different classes can be used interchangeably if they implement the same interface:

```python
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(animal.speak())  # Each animal makes its own sound
```

### 4. Abstraction
Hiding complex implementation details and exposing only essential features:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
```

## Naming Conventions

- **Classes**: `CamelCase` (e.g., `MyClass`, `DatabaseConnection`)
- **Methods and functions**: `snake_case` (e.g., `my_method`, `process_data`)
- **Constants**: `UPPER_CASE` (e.g., `MAX_SIZE`, `PI`)
- **Private attributes**: `_single_underscore` or `__double_underscore`

## Special Methods (Dunder Methods)

```python
class Person:
    def __init__(self, name):      # Constructor
        self.name = name
    
    def __str__(self):             # String representation
        return f"Person: {self.name}"
    
    def __repr__(self):            # Official representation
        return f"Person('{self.name}')"
    
    def __len__(self):             # Length
        return len(self.name)
    
    def __eq__(self, other):       # Equality
        return self.name == other.name
```

## Benefits of OOP

- **Modularity**: Code is organized into logical, reusable units
- **Maintainability**: Easier to understand and modify code
- **Reusability**: Classes and objects can be reused across projects
- **Extensibility**: New functionality can be added through inheritance
- **Flexibility**: Polymorphism allows for flexible, generic code

