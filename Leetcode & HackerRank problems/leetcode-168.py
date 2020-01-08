class Solution:
    def convertToTitle(self, n: int) -> str:
        self.alph = list('_ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return self.helper(n)
        
    def helper(self, n):
        if n <= 26: return self.alph[n]
        if n%26 == 0: return self.helper(n//26-1) + self.alph[n%26-1]
        else: return self.helper(n//26) + self.alph[n%26]
