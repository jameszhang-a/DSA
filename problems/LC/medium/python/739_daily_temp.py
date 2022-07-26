"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no future
day for which this is possible, keep answer[i] == 0 instead.



Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [1, 2, 3, 2, 1, 4]
        [3]

        [4, 3, 2, 1, 5]
        """
        n = len(temperatures)
        output = [0] * n
        s = []

        for i, temp in enumerate(temperatures):
            while s and temp > temperatures[s[-1]]:
                cooler_i = s.pop()
                output[cooler_i] = i - cooler_i

            s.append(i)

        return output

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.dailyTemperatures(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[4, 3, 2, 1, 5]],
    [[73, 74, 75, 71, 69, 72, 76, 73]],
    [[30, 40, 50, 60]],
    [[30, 60, 90]],
]
expected = [
    [4, 3, 2, 1, 0],
    [1, 1, 4, 2, 1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 0],
]


sol = Solution()
sol.test(input, expected)
