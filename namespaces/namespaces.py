# Namespaces are a mapping from names to objects.
# They are used to avoid confusion in the global scope.
# The global namespace is the dictionary of the current module.
# The local namespace is the dictionary of the current function.
# The built-in namespace is the dictionary of the built-in functions.


# built-in namespace
print(dir(__builtins__))

a = 'global'
# global namespace
print(globals())

print(globals().get('a', 'not found'))

# local namespace
def func():
    a = 'local to func'
    print(locals())

func()


def nfunc():
    a = 'local to nfunc'
    def nnfunc():
        a = 'local to nnfunc'
        print(locals())
    print(locals())
    nnfunc()

nfunc()




def bar(a='default'):
    print(locals())

bar()


