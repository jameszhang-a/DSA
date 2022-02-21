from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Input:
        gas  =  [1,2,3,4,5]
        cost =  [3,4,5,1,2]
        """
        curr, total = 0, 0
        start = 0

        for i in range(len(gas)):
            extra = gas[i] - cost[i]
            curr += extra
            total += extra
            if curr < 0:
                start = i + 1
                curr = 0

        return -1 if total < 0 else start


sol = Solution()
gas = [5, 8, 2, 8]

cost = [6, 5, 6, 6]


print(sol.canCompleteCircuit(gas, cost))
