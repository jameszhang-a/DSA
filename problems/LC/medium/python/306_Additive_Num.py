"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the 
sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function 
to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, 
so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:
Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(s, seq):

            if not s:
                if len(seq) > 2:
                    print('TRUU')
                    return True
                else:
                    print('FALSE')
                    return False

            for i in range(len(s)):
                print(f"\nString: {s}, Sequence: {seq}, Iteration: {i} ")
                if s[0] == '0' and i > 0:
                    break

                cur = int(s[:i+1])

                if len(seq) > 1 and cur != seq[-2] + seq[-1]:
                    print(f"Comparing cur: {cur} != {seq[-2]} + {seq[-1]}")
                    continue

                if dfs(s[i+1:], seq+[cur]):
                    print(f"New search: ({s[i+1:]}, {seq+[cur]})")
                    return True
                
            return False

        return dfs(num, [])


sol = Solution()
print(sol.isAdditiveNumber("199100199"))
