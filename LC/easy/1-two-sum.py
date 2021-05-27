class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = [None]*2
        for x in range(len(nums)-1):
            temp = len(nums)-1-x
            for y in range(temp):
                if nums[x] + nums[x+1+y] == target:
                    out[0]=x
                    out[1]=x+1+y
                    
        return out
        