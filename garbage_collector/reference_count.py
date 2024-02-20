import sys
import gc


my_obj = {}
# The reference count of the object is 1
# Note that sys.getrefcount() returns the number of references to the object + 1
# as it also creates a reference to the object
print("Reference count:", sys.getrefcount(my_obj))

# Create another reference to the object
another_reference = my_obj
# The reference count of the object is 2 + 1
print("Reference count:", sys.getrefcount(my_obj))

# Delete the reference
del another_reference
# The reference count of the object is 1 + 1
print("Reference count:", sys.getrefcount(my_obj))


def foo(obj):
    # The reference count of the object is increased by 2
    # one reference for the caller and one reference for the function's local namespace
    print("Reference count:", sys.getrefcount(obj))


# The reference count of the object is 3 + 1
foo(my_obj)
# The reference count of the object is 1 + 1
print("Reference count:", sys.getrefcount(my_obj))
