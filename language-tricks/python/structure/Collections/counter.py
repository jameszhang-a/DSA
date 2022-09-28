from collections import Counter

# use counter for counting things duh
# similar use cases as defaultdict but not quite

# Counter object is like a bag of stuff

word = "mississippi"

count = Counter(word)  # returns a Counter object, basically a dict

to_dict = dict(count)  # {'i': 4, 's': 4, 'p': 2, 'm': 1}
to_list = list(count)  # ['m', 'i', 's', 'p']


#######################
### if a contains b ###
#######################

counter_1 = Counter("ababa")
counter_2 = Counter("abb")

# to check if counter 1 contains all of counter 2
counter_2 - counter_1

print(not (counter_2 - counter_1))  # true, counter 1 does contain 2

######################
### some functions ###
######################

# different ways to initialize
x = Counter(apples=5, oranges=10)
y = Counter({"bananas": 3, "peaches": 8})

a = dict(x)  # { apples: 5, oranges: 10 }
b = dict(y)  # { bananas: 3, peaches: 8 }


# elements()

display_fruits = x.elements()  # <class 'itertools.chain'>
to_list = list(display_fruits)
# ['apples', 'apples', 'apples', 'apples', 'apples',
# 'oranges', 'oranges', 'oranges', 'oranges', 'oranges',
# 'oranges', 'oranges', 'oranges', 'oranges', 'oranges']


x.items()
# dict_items([('apples', 5), ('oranges', 10)])

x.keys()
# dict_keys(['apples', 'oranges'])

x.total()
# 15 (sum of all counts)

x.update(apples=5)
# apple now has 10

x.most_common(1)
# [('apples', 10)]


# Set interaction

# Fruit sold per day
sales_day1 = Counter(apple=4, orange=9, banana=4)
sales_day2 = Counter(apple=10, orange=8, banana=6)

# Total sales
sales_day1 + sales_day2
Counter({"orange": 17, "apple": 14, "banana": 10})

# Sales increment
sales_day2 - sales_day1
Counter({"apple": 6, "banana": 2})

# Minimum sales
sales_day1 & sales_day2
Counter({"orange": 8, "apple": 4, "banana": 4})

# Maximum sales
sales_day1 | sales_day2
Counter({"apple": 10, "orange": 9, "banana": 6})


# Im guessing set operations work because of elements() works
# that's because python is treating it like a bag of stuff, ie, a set
# Except it's a set that can have duplicates and it counts it


### Negative values ###
more_fruits = Counter(apple=5, pear=-3, cherry=6)

more_fruits
# Counter({'cherry': 6, 'apple': 5, 'pear': -3})

+more_fruits
# Counter({'cherry': 6, 'apple': 5})

-more_fruits
# Counter({'pear': 3})
