# unpack "*", "**", is similar to JS spread "..."

a = [1, 2, 3, 4, 5]
print(a)  # [1, 2, 3, 4, 5]

# same thing
print(*a)  # 1 2 3 4 5
print(1, 2, 3, 4, 5)


# When used in parameter,
# turn all arguments into a tuple
def fun(*num):
    return type(num)  # tuple


print(fun(1, 2))  # tuple

# Useful for take in an unknown number of prarams
def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum(5, 4, 3, 2, 1))  # 15


# For adding two lists
listA = ["a", "b", "c", "d"]
listB = [9, 8, 7, 6]

listA = [*listA, *listB]
