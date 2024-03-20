
# defining 'a' in the global namespace
a = 'global'


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
