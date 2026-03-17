import copy

import pandas as pd

# mutable dictionaries
a = {'a': 1, 'aa': 2}
b = {'b': 3, 'bb': {'c': -1}}

d = {'A': [a], 'B': [b]}

# mutable dataframe
df = pd.DataFrame(d)

print(df)

def foo(df):
    df['A'][0]['a'] = 5
    df['B'][0]['b'] = 6
    df['B'][0]['bb']['c'] = -2

foo(df)

print("df", df)

def foo_shallowcopy(df):
    df_tmp = df.copy(deep=False)  # shallow copy of the dataframe
    print("pandas shallow copy dataframe are the same objects", df is df_tmp)
    print("pandas shallow copy dataframe values are the same objects", df['A'][0] is df_tmp['A'][0])
    print("pandas shallow copy dataframe nested dict values are the same object",
          df['B'][0]['bb'] is df_tmp['B'][0]['bb'])
    df_tmp['A'][0]['a'] = 7
    df_tmp['B'][0]['b'] = 8
    df_tmp['B'][0]['bb']['c'] = -3
    return df_tmp

df_shallowcopy = foo_shallowcopy(df)
print("df_shallowcopy", df_shallowcopy)
print("df", df)


def foo_copy(df):
    df_tmp = df.copy()  # deep=True by default copy of the dataframe
    print("pandas copy dataframe are the same objects", df is df_tmp)
    print("pandas copy dataframe values are the same objects", df['A'][0] is df_tmp['A'][0])
    print("pandas copy dataframe nested dict values are the same object",
          df['B'][0]['bb'] is df_tmp['B'][0]['bb'])
    df_tmp['A'][0]['a'] = 7
    df_tmp['B'][0]['b'] = 8
    df_tmp['B'][0]['bb']['c'] = -3
    return df_tmp

df_copy = foo_copy(df)
print("df_copy", df_copy)
print("df", df)

def foo_deepcopy(df):
    df_tmp = df.map(copy.deepcopy)  # custom deep copy of the dataframe makes a deep copy on the nested elements of the dataframe
    print("pandas custom deep copy dataframe are the same objects", df is df_tmp)
    print("pandas custom deep copy dataframe values are the same objects", df['A'][0] is df_tmp['A'][0])
    print("pandas custom deep copy dataframe nested dict values are the same object",
          df['B'][0]['bb'] is df_tmp['B'][0]['bb'])
    df_tmp['A'][0]['a'] = 9
    df_tmp['B'][0]['b'] = 10
    df_tmp['B'][0]['bb']['c'] = -4
    return df_tmp

df_deepcopy = foo_deepcopy(df)
print("df_deepcopy", df_deepcopy)
print("df", df)

# changing the value of a nested element from outside the dataframe
a['a'] = 11

print("df", df)
print("df_copy", df_copy)
print("df_deepcopy", df_deepcopy)


# copies on dataframe slices
# df['A'] is a view of the original dataframe
# df_fil is a shallow copy of the original dataframe
df_fil = df['A'].copy(deep=False) # with no deep copy the original dataframe is modified

print("comparing dataframe slices: df['A'] and df_fil are the same object:", df['A'] is df_fil)
print("comparing dataframe values: df['A'][0] and df_fil[0] are the same object:", df['A'][0] is df_fil[0])


df_fil[0]['a'] = 12
print("df", df)
print("df_fil", df_fil)

df_fil[0] = {'a': 13}
# both the original dataframe and the shallow copy are modified
print("df", df)
print("df_fil", df_fil)


# df_fil is a deep copy of the original dataframe
df_fil = df['A'].copy() # deep=True by default

print("comparing dataframe slices: df['A'] and df_fil are the same object:", df['A'] is df_fil)
print("comparing dataframe values: df['A'][0] and df_fil[0] are the same object:", df['A'][0] is df_fil[0])

# Python objects are not copied, only references to the objects are copied
df_fil[0]['a'] = 14
# both the original dataframe and the deep copy are modified, since the mutable object (dict) is not copied
print("df", df)
print("df_fil", df_fil)


# reassigning the value of the slice
df_fil[0] = {'a': 15}

# only the copy is modified
print("df", df)
print("df_fil", df_fil)

# deep copy of the dataframe, deep copy of the nested elements
df_fil = df['A'].copy().map(copy.deepcopy) # deep=True by default
print("comparing dataframe slices: df['A'] and df_fil are the same object:", df['A'] is df_fil)
print("comparing dataframe values: df['A'][0] and df_fil[0] are the same object:", df['A'][0] is df_fil[0])

# Python objects are copied
df_fil[0]['a'] = 16
# both the original dataframe and the deep copy are modified, since the mutable object (dict) is not copied
print("df", df)
print("df_fil", df_fil)
