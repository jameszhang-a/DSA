def twoSum(nums, target: int):
    tb = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in tb:
            return [tb[diff], i]
        else:
            tb[num] = i


print(twoSum([3, 3], 6))
