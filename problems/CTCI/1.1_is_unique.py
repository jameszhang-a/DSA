
# ? Implement an algorithm to check if a string only has unique values
# ? What if no additional data structures

class Solution:
    def isUnique_1(self, s: str) -> bool:
        """ 
        Dictionary/Hash table implementation 
            Time:   O(N) 
            Space:  O(N)
        """

        dic = {}
        for c in s:
            if c in dic:
                return False
            dic[c] = 1
        return True

    def isUnique_2(self, s: str) -> bool:
        """
        No data structure 
            Time:   O(N)
            Space:  O(1)
        """
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    return False
        return True

    def isUnique_3(self, s: str) -> bool:
        """
        Assuming 128 ASCII chars
            Time:   O(1) since array is 128 fixed
            Space:  O(1)
        """

        chars = [False] * 128

        for c in s:

            # Get unicode/ascii value of char
            idx = ord(c)
            if chars[idx]:
                return False
            chars[idx] = True

        return True


sol = Solution()
print(sol.isUnique_1('1bsa9h32.!'))
print(sol.isUnique_2('1bsa9h32.!'))
print(sol.isUnique_3('1bsa9h32.!'))
