import copy

l = ['a', ['b', ['c', ['d']]]]

print(l)

# shallow copy copies the object but not nested objects
l_copy = l.copy()

# deep copy copies the object and all nested objects
l_deepcopy = copy.deepcopy(l)

# changing the value of a nested element
l[1][1][1] = 'X'

print(l)
print(l_copy)
print(l_deepcopy)


d = {'a': {'b': {'c': {'d': 1}}}}

print(d)

# shallow copy copies the object but not nested objects
d_copy = d.copy()
# deep copy copies the object and all nested objects
d_deepcopy = copy.deepcopy(d)

# changing the value of a nested element
d['a']['b']['c'] = 2

print(d)
print(d_copy)
print(d_deepcopy)
