# Careful when defining a function, you may be overriding a built-in function

def foo():
    # here we are overriding the built-in function 'print'
    # with a print function that does nothing
    def print(*args, **kwargs):
        pass
    print('foo')  # this will not print anything
    __builtins__.print('foo')  # this will print 'foo'

foo()

# The built-in function 'print' is overridden by the function 'print' defined in the local namespace of 'foo'
# so it does not affect the built-in function 'print' in the global namespace
print('foo')  # this will print 'foo'


# if we override the built-in function 'print' in the global namespace
def print(*args, **kwargs):
    __builtins__.print('overridden print')


# The print function is overridden in the global namespace
print('foo')  # this will print 'overridden print'
__builtins__.print('foo')  # this will print 'foo'
