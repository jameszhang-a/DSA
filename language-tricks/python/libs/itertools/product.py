from itertools import product, permutations, combinations

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#### normal way ####
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])  # 1,2,...,12

### with product ###
for i, j in product(range(len(matrix)), range(len(matrix[0]))):
    print(matrix[i][j])  # 1,2,...,12

# all possibale matches
print(list(product("ABC", repeat=2)))

# all permutations, no dups, i.e. no (A, A)
print(list((permutations("ABC", 2))))

# all combinations, no repeats, no (A, B), (B, A)
print(list(combinations("ABC", 2)))
