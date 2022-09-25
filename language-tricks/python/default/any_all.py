# Returns true if any of the list is true, false otherwise
# Similar to some() in JS

list = [True, False, False, True]
list_false = [False, False]

half = any(list)  # true

false = any(list_false)  # false


# Use lambda/key to define rules doesn't work
list_num = [1, 2, 4, 6, -6]

# ! doesn't work
# odd_any = any(list_num, key=lambda x: x % 2 == 1)

# Convert into true/false list
odd_list = [(lambda x: x % 2 == 1)(num) for num in list_num]
odd = any(odd_list)

# Or combind them
odd_one_line = any([(lambda x: x % 2 == 1)(num) for num in list_num])

print(odd == odd_one_line)  # true


## 'all' works the same way

list_true = [True, True, True]
all_true = all(list_true)  # true

some_false = [True, True, False]
one_false = all(some_false)  # false
