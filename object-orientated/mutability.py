
# Mutability
# lists are mutable, they can be changed in place after creation
a = []
old_id = id(a)

# changing the value of a
a.append(1)
# the id of a is the same as before; id(a) == old_id
print('old_id:', old_id, 'new_id:', id(a), ' -> same' if old_id == id(a) else ' -> different')

# Below the object referenced by d is changed, therefore c is also changed
c = d = []
print('c is d:', c is d, f'{c=}, {d=}')
d.append(1)
print('c is d:', c is d, f'{c=}, {d=}')

# Immutability
# strings are immutable, they cannot be changed after creation
a = 'hello'
old_id = id(a)

# changing the value of a
a += ' world'
# the id of a is different than before; id(a) != old_id
print('old_id:', old_id, 'new_id:', id(a), ' -> same' if old_id == id(a) else ' -> different')

# Below d is reassigned to a new object whereas c is not
c = d = 'hello'
print('c is d:', c is d, f'{c=}, {d=}')
d += ' world'
print('c is d:', c is d, f'{c=}, {d=}')
