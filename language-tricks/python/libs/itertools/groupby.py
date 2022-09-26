from itertools import groupby


"""
groupby returns an iterator with the key and a grouper object of the occurrence of the key

MUST be in order, or the groups are messed up
"""


a = [1, 2, 1, 3, 3, 4, 4, 4, 1]

for i in groupby(a):
    print(i)
    x, y = i
    print(x, list(y))

"""
result:
1: [1]
2: [2]
1: [1]
3: [3, 3]
4: [4, 4, 4]
1: [1]
"""

b = [("a", 3), ("b", 2), ("a", 1), ("a", 8)]

key_fun = lambda x: x[0]

for x, y in groupby(b, key_fun):
    print(x, list(y))

"""
result:
a [('a', 3)]
b [('b', 2)]
a [('a', 1), ('a', 8)]
"""
