from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float("inf")

        for i in range(len(prices) - 1):
            if prices[i] < low:
                low = prices[i]

            diff = prices[i + 1] - low
            if diff > profit:
                profit = diff

        return profit


s = Solution()
print(s.maxProfit([13, 5, 6, 1, 9]))
