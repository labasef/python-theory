# Namespaces are a mapping from names to objects.
# They are used to avoid confusion in the global scope.
# The global namespace is the dictionary of the current module.
# The local namespace is the dictionary of the current function.
# The built-in namespace is the dictionary of the built-in functions.

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



def foo(a):
    # implicitly a variable 'a' is created in the local namespace of foo
    # such as a (local) = a (global)
    print(locals())
    # we can see that it is the same object referenced by 'a', both locally and globally
    print('local "a" is global "a": ', locals().get('a') is globals().get('a'))
    # local namespace is reassigned
    a = 'local to foo'
    # local namespace is changed
    print(locals().get('a', 'not found'))
    # global namespace is not changed
    print(globals().get('a', 'not found'))
    print('local "a" is global "a": ', locals().get('a') is globals().get('a'))

foo(a)

def moo(b):
    # implicitly a variable 'a' is created in the local namespace of foo
    # such as a (local) = a (global)
    print(locals())
    # we can see that it is the same object referenced by 'a', both locally and globally
    print('local "b" is global "b": ', locals().get('b') is globals().get('b'))
    # mutable list is changed
    b.append('local to foo')
    # local namespace is changed
    print(locals().get('b', 'not found'))
    # global namespace is changed
    print(globals().get('b', 'not found'))
    print('local "b" is global "b": ', locals().get('b') is globals().get('b'))

b= ['global']
moo(b)


# built-in namespace
print(dir(__builtins__))
