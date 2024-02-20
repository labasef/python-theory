import sys
import gc


my_obj = {}
# The reference count of the object is 1
# Note that sys.getrefcount() returns the number of references to the object + 1
# as it also creates a reference to the object
print("Reference count:", sys.getrefcount(my_obj))

# Create another reference to the object
another_reference = my_obj
# The reference count of the object is 2
print("Reference count:", sys.getrefcount(my_obj))

# Delete the reference
del another_reference
# The reference count of the object is 1
print("Reference count:", sys.getrefcount(my_obj))
