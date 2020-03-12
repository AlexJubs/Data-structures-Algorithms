class Solution:
    def __init__(self):
        self.dp = dict()
        self.dp[0] = 0
        self.dp[1] = 1
        self.dp[2] = 1
        
    def tribonacci(self, n: int) -> int:
        if n in self.dp: return self.dp[n]
        self.dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.dp[n]
