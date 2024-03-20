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
    print("pandas shallow copy dataframe ids", id(df), id(df_tmp))
    print("pandas shallow copy nested ids", id(df['A'][0]), id(df_tmp['A'][0]))
    print("custom deep copy most nested ids", id(df['B'][0]['bb']), id(df_tmp['B'][0]['bb']))
    df_tmp['A'][0]['a'] = 7
    df_tmp['B'][0]['b'] = 8
    df_tmp['B'][0]['bb']['c'] = -3
    return df_tmp

df_shallowcopy = foo_shallowcopy(df)
print("df_shallowcopy", df_shallowcopy)
print("df", df)


def foo_copy(df):
    df_tmp = df.copy()  # deep=True by default copy of the dataframe
    print("pandas deep copy dataframe ids", id(df), id(df_tmp))
    print("pandas deep copy nested ids", id(df['A'][0]), id(df_tmp['A'][0]))
    print("custom deep copy most nested ids", id(df['B'][0]['bb']), id(df_tmp['B'][0]['bb']))
    df_tmp['A'][0]['a'] = 7
    df_tmp['B'][0]['b'] = 8
    df_tmp['B'][0]['bb']['c'] = -3
    return df_tmp

df_copy = foo_copy(df)
print("df_copy", df_copy)
print("df", df)

def foo_deepcopy(df):
    df_tmp = df.map(copy.deepcopy)  # custom deep copy of the dataframe makes a deep copy on the nested elements of the dataframe
    print("custom deep copy dataframe ids", id(df), id(df_tmp))
    print("custom deep copy nested ids", id(df['A'][0]), id(df_tmp['A'][0]))
    print("custom deep copy most nested ids", id(df['B'][0]['bb']), id(df_tmp['B'][0]['bb']))
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