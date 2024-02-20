import sys
# everything is an object
print(isinstance(None, object))
# literals are objects
print(isinstance('hello', object))
print(isinstance(4, object))
# lists, tuples, and dictionaries are objects
print(isinstance([], object))
print(isinstance((), object))
print(isinstance({}, object))
# modules are objects
print(isinstance(sys, object))
# classes are objects
print(isinstance(str, object))
# functions are objects
print(isinstance(print, object))
