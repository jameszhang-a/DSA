
# ? given 2 strings, check if one is a permutation of another
"""
Case 1: False
s1 = abc
s2 = uthenacb

Case 2: True
s1 = applecar
s2 = racapple
"""

"""
Approach: 
sort both strings, they have to be the same

"""


class Solution:
    def permutation_1(self, s1: str, s2: str) -> bool:
        """
        Python sorted() is timsort with O(n log n)
            Time:   O(n log n)
            Space:  O(1)
        """
        return sorted(s1) == sorted(s2)

    def permutation_2(self, s1: str, s2: str) -> bool:
        """
        Using a dictionary to check each string has the same 
        frequency of chars
            Time:   O(n)
            Space:  O(n)
        """

        checked = dict()

        # count how many times each char appear in the fi
        for c in s1:
            if not c in checked:
                checked[c] = 1
            else:
                checked[c] += 1

        for c in s2:
            if not c in checked or checked[c] < 0:
                return False

            checked[c] -= 1

        return True


sol = Solution()
print(sol.permutation_1('applecar', 'racapple'))
print(sol.permutation_2('applecar', 'racapple'))
