"""
A person running up stairs with n steps can go either 1,2,or 3 steps at a time,
Implement a method to count how many ways the person can run up the stairs
"""


def triple_step(n: int):
    """DP method"""
    a, b, c = 1, 2, 4

    for n in range(3, n):
        a, b, c = b, c, a + b + c

    # this is ugly but whatever
    return 0 if n == 0 else a if n == 1 else b if n == 2 else c


def print_triple(n: int):
    for i in range(n):
        print(triple_step(i))


print_triple(40)
