# Regular function
def square(num):
    return num * num


print(square(9))


# Lambda version
square_2 = lambda num: num * num

print(square_2(5))


## more exploration
age = 30

# Adding () around lambda,
# and you can call it directly with a param
is_old = (lambda x: x > 50)(age)

print(is_old)  # false
