num = max(1, 2, 3)  # 3

char = max("a", "b", "c")  # c

list = [1, 2, -5, 4]
max_list = max(list)  # 4

# Cann accept a key to change rule
# Returns number with largest square
max_key = max(list, key=lambda x: x * x)  # -5

# Works with min too
min_key = min(list, key=lambda x: x * x)  # -5
