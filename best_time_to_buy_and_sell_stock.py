class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        mini = prices[0]
        res = 0
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            res = max(res, prices[i]-mini)
        return res
