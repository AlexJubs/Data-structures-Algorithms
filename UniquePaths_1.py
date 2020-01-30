class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        self.hash_t = {}
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1: return 0
        return self.uniquePaths(0, 0)
    
    def uniquePaths(self, m: int, n: int) -> int:
        if self.hash_t.get(str(m)+'|'+str(n)) != None:
            return self.hash_t[str(m)+'|'+str(n)]
        
        if m >= len(self.grid[0]) or n >= len(self.grid):
            self.hash_t[str(m)+'|'+str(n)] = 0
            return 0
        
        if (self.grid[n][m] == 1):
            self.hash_t[str(m)+'|'+str(n)] = 0
            return 0
        
        if m == len(self.grid[0])-1 and n == len(self.grid)-1:
            self.hash_t[str(m)+'|'+str(n)] = 1
            return 1
        
        self.hash_t[str(m)+'|'+str(n)] = self.uniquePaths(m+1,n) + self.uniquePaths(m,n+1)
        return self.hash_t[str(m)+'|'+str(n)]