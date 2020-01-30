class Solution:
    def mapping(self, N):
        if self.dp.get(N) != None: return self.dp[N]
        self.dp[N] = N-1+self.mapping(N-1)
        return N-1+self.mapping(N-1)
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        self.dp = {0:0, 1:0, 2:1}
        freq = dict()
        for x in dominoes:
            if freq.get(tuple(sorted(x))) != None:
                freq[tuple(sorted(x))] = freq[tuple(sorted(x))] + 1
            else: freq[tuple(sorted(x))] = 0
        res = 0
        for x in freq.values():
            res = res+ self.mapping(x+1)
        return res