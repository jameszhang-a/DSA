class Solution:
    def tribonacci(self, n: int, dp: dict = {0: 0, 1: 1, 2: 1}) -> int:
        """Simple DP solution"""
        if n not in dp:
            dp[n] = self.tribonacci(
                n-3, dp) + self.tribonacci(n-2, dp) + self.tribonacci(n-1, dp)

        return dp[n]
    
    def tribonacci_3(self, n: int)-> int:
        """keeping track of the last 3 items"""
        a,b,c = 0,1,1
        
        for i in range(n):
            a,b,c = b,c,a+b+c
        
        return a