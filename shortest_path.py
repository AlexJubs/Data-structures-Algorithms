class Solution:
    def __init__(self):
        self.hash_t = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 0 or n < 0: return 0
        if self.hash_t.get(str(m)+'|'+str(n)) != None:
            return self.hash_t[str(m)+'|'+str(n)]
        if m == 0 and n == 0:
            self.hash_t[str(m)+'|'+str(n)] = 0
            return 0
        if m == 1 or n == 1:
            self.hash_t[str(m)+'|'+str(n)] = 1
            return 1
        self.hash_t[str(m)+'|'+str(n)] = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        return self.hash_t[str(m)+'|'+str(n)]