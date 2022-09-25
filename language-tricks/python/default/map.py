nums = [2, 4, 6, 8, 10]

# Creates a 'map' object, that can only be iterated once
# takes in a function and a collection
doubles = map(lambda x: x * 2, nums)

# Usually we want a list
list_doubles = list(map(lambda num: num * 2, nums))


# Can also take in regular function
def double(num):
    return num * 2


list_doubles_2 = list(map(double, nums))

print(list_doubles == list_doubles_2)  # true


## Want to make upercase
people = ["james", "gene", "bob"]

big_people = list(map(lambda person: person.upper(), people))
