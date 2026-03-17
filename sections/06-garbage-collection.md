# Garbage Collection

Garbage collection is the automatic process of freeing memory by identifying and removing objects that are no longer in use. Python uses a combination of reference counting and cycle detection for garbage collection.

## Reference Counting

Python's primary garbage collection mechanism is **reference counting**:
- Each object has a count of how many references point to it
- When an object is referenced, the count increases
- When a reference is removed, the count decreases
- When the count reaches zero, the object is immediately deallocated

### Example
```python
import sys

a = []           # Reference count: 1
b = a            # Reference count: 2
c = a            # Reference count: 3
del b            # Reference count: 2
del c            # Reference count: 1
del a            # Reference count: 0, object is deallocated

print(sys.getrefcount(obj))  # Returns the reference count
```

## Circular References

A problem occurs when objects reference each other (circular references):
```python
a = []
b = []
a.append(b)  # a refers to b
b.append(a)  # b refers to a

del a
del b
# Objects still exist in memory because they reference each other
# Reference counts are both 1 (from their mutual references)
```

## Cycle Detection

Python has a generational garbage collector to handle circular references:
- Objects are grouped into three generations (0, 1, 2)
- Younger generations are collected more frequently
- When a cycle is detected, all objects in the cycle are deallocated

### The `gc` Module
```python
import gc

# Trigger garbage collection manually
gc.collect()

# Get information about collected objects
collected = gc.collect()
print(f"Collected {collected} objects")

# Disable automatic collection
gc.disable()

# Re-enable automatic collection
gc.enable()

# View objects with circular references
for obj in gc.garbage:
    print(obj)
```

## Best Practices

1. **Understand reference counting**: Be aware of object lifetime in your code
2. **Break circular references**: Use weak references when appropriate
3. **Avoid unnecessary object retention**: Delete objects you no longer need
4. **Use context managers**: `with` statements properly handle resource cleanup
5. **Profile memory usage**: Identify memory leaks in your applications

## Monitoring Garbage Collection

```python
import gc

# Get garbage collector statistics
stats = gc.get_stats()
print(stats)

# Disable collection for performance-critical code
with gc.disabled():
    # Performance-critical code here
    pass
```

---
[← Previous: Python Interpreter](05-python-interpreter.md) | [Home](../README.md) | [Next: Object-Orientated →](07-object-orientated.md)
---
