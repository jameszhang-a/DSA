import sys

list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x for x in range(1000))

print("to do the same thing...")
print(f"List Comprehension takes [{list_comp}] bytes")  # 8856
print(f"Generator Expression takes [{gen_exp}] bytes")  # 112
