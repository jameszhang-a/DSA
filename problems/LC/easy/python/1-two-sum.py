def twoSum(nums, target: int):
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]], i]
        dict[nums[i]] = i
        diff = target-nums[i]
        
        if diff in dict and dict[diff] != i:
            return [dict[diff], i]

print(twoSum([3, 3], 6))