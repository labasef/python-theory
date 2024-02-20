a = [1]
c = b = [1]

# a and b reference two different objects
print(a is b)
print(b is c)

# a and b have the same value
print(a == b)
print(b == c)

# Since a and b reference two different objects, the id of a and b are different
print('id_a', id(a), 'id_b', id(b), 'id_c', id(c))
