"""
dfs, create a set and add the path to it, if we hit an element we're seen before, end. return len of the set
"""
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self.A = nums
        self.dp = dict()
        self.S = set()
        res = 0
        for i in range(len(nums)):
            self.S = set()
            res = max(res,self.trav(i))
        return res

    def trav(self, ind):
        if self.dp.get(ind) != None: return self.dp[ind]
        if ind in self.S:
            for elem in list(self.S):
                self.dp[elem] = len(self.S)
            return len(self.S)
        self.S.add(ind)
        return self.trav(self.A[ind])
