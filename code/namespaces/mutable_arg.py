b = ['global']

def moo(b):

    # implicitly a variable 'b' is created in the local namespace of foo
    # such as b (local) = b (global)
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

moo(b)

# variable b from the global scope is changed
print(b)