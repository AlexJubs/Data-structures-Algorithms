class Solution:
    def layers(self, Y: int, res: int):
        if (Y == self.X): return res
        if (Y%2 == 0) and (Y > self.X): return self.layers(Y/2,res+1)
        else: return self.layers(Y+1,res+1)
        
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y < X and Y == 1: return X-Y
        self.X = X
        return self.layers(Y,0)