import time


class Solution:
    def fib(self, n: int) -> int:
        """Simple recursion solution"""
        if n == 1:
            return 1
        elif n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)

    def fib_dp(self, n: int, dp: dict = {0: 0, 1: 1}) -> int:
        """Implement dynamic programming method"""
        if n not in dp:
            dp[n] = self.fib_dp(n-1) + self.fib_dp(n-2)
        else:
            return dp[n]

        return dp[n]


sol = Solution()

start = time.time()
ans = sol.fib(35)
end = time.time()
print(f"recursion - ans: {ans}, time: {end-start}")


start = time.time()
ans = sol.fib_dp(250)
end = time.time()
print(f"dp - ans: {ans}, time: {end-start}")
