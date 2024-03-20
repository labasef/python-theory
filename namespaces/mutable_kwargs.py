# the function definition has its own namespace
# the keyword arguments are defined there
# Thus, using mutable objects as default arguments can lead to unexpected behavior

def foo(a=[]):
    a.append(1)
    print(a)

for i in range(3):
    foo()


# The values of mutable default arguments are shared between calls
# Thus, if the value of 'a' is changed in one call, it will be changed in all subsequent calls
