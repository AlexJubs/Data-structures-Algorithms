class Solution: 
    def helper (self, para, opened, closed):
        if opened > self.n or closed > self.n: return
        if opened == self.n and closed == self.n: self.res.append(para)
        if opened > closed:
            self.helper(para +')', opened, closed+1)
            self.helper(para +'(', opened+1, closed)
        elif opened == closed:
            self.helper(para +'(', opened+1, closed)
            
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res = list()
        self.helper('(', 1,0)
        return self.res