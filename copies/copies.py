import copy

# lists are mutable, they can be changed in place after creation
# original list 'l' with nested lists
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

# dictionaries are mutable, they can be changed in place after creation
# original dictionary 'd' with nested dictionaries
d = {'a': {'b': {'c': {'d': 1}}}}

print(d)

# shallow copy copies the object but not nested objects
d_copy = d.copy()
print("d and d_copy are the same object:", d is d_copy)
print("nested dictionaries d['a'] and d_copy['a'] are the same object:", d['a'] is d_copy['a'])

# deep copy copies the object and all nested objects
d_deepcopy = copy.deepcopy(d)
print("d and d_deepcopy are the same object:", d is d_deepcopy)
print("nested dictionaries d['a'] and d_deepcopy['a'] are the same object:", d['a'] is d_deepcopy['a'])

# changing the value of a nested element in the original dictionary
d['a']['b']['c'] = 2

print(d)
print(d_copy)
print(d_deepcopy)
