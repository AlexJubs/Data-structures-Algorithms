class Solution:
    def trav(self, seq):
        if len(seq) == self.N: 
            self.res.add(int(seq))
            return
        if int(seq[-1])-self.diff >= 0: self.trav(seq + str(int(seq[-1])-self.diff))
        if int(seq[-1])+self.diff < 10: self.trav(seq + str(int(seq[-1])+self.diff))
        
    def numsSameConsecDiff(self, N, K):
        if N == 1: return [0,1,2,3,4,5,6,7,8,9]
        self.N = N
        self.diff = K
        self.res = set()
        for i in range(1,10):
            self.trav(str(i))
        return list(self.res)