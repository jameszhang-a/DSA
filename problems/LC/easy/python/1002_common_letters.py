"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates).
You may return the answer in any order.


Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Count frequency of letter in the first word
        """
        first = Counter(words[0])
        print(first)

        # {'l': 2, 'b': 1, 'e': 1, 'a': 1}
        for i in range(1, len(words)):
            word = words[i]
            count = Counter(word)
            for k in list(first):
                if k not in word:
                    del first[k]
                    continue
                else:
                    first[k] = min(first[k], count[k])

        res = list()
        for k, v in first.items():
            for i in range(v):
                res.append(k)

        return res


sol = Solution()
words = ["bellla", "label", "roller"]


print(sol.commonChars(words))
