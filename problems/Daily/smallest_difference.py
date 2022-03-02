"""
nums = [6, 2, 5, 3, 1], return [[1, 2], [2, 3], [5, 6]].
"""


def smalldiff(arr):
    S = sorted(arr)

    ans = []
    diff = -1

    for i in range(len(S) - 1):
        if diff == -1:
            diff = S[i + 1] - S[i]
        if S[i + 1] - S[i] == diff:
            ans.append([S[i], S[i + 1]])
    return ans


nums = [4, 2, 3]
print(smalldiff(nums))
