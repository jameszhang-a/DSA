from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        txt = Counter(text)
        return min(txt["b"], txt["a"], txt["n"], txt["l"] // 2, txt["o"] // 2)


sol = Solution()
text = "nlaebolko"

print(sol.maxNumberOfBalloons(text))
