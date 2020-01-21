class Solution:
    phone = {1:[6,8], 2:[7,9], 3:[8,4], 4:[0,3,9], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4], 0:[4,6]}
    def knightDialer(self, N: int) -> int:
        if N == 1: return 10
        self.dp = {(1,1): 2,
                   (2,1): 2,
                   (3,1): 2,
                   (4,1): 3,
                   (6,1): 3,
                   (7,1): 2,
                   (8,1): 2,
                   (9,1): 2,
                   (0,1): 2}
        self.build_dp(N)
        self.res = 0
        for i in range(1,10):
            if i != 5:
                self.trav(i, N)
        return (self.res//2)%(10**9+7)
        
    def build_dp(self, N):
        for moves in range(1,N):
            for pos in range(10):
                if pos != 5:
                    if self.dp.get((pos,moves)) == None:
                        temp = 0
                        for x in self.phone[pos]:
                            temp = temp + self.dp[(x,moves-1)]
                            
                        self.dp[(pos,moves)] = temp
        
    def trav(self, pos, N):
        if self.dp.get((pos,N)) != None:
            self.res = self.res+self.dp[(pos,N)]
            return
        for next_pos in self.phone[pos]:
            self.trav(next_pos, N-1)
