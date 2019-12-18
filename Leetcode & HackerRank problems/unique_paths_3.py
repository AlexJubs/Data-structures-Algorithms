class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.grid = grid
        self.numZeros = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: self.numZeros += 1
                if grid[i][j] == 1: start = (i,j)
        self.trav(start[0], start[1], set())
        return self.res
    
    def trav(self, i, j, path):
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]): return
        if self.grid[i][j] == -1: return
        if self.grid[i][j] == 2:
            if len(path) > self.numZeros:
                self.res = self.res+1
            return
        if (i,j) in path: return
        self.trav(i+1, j, path.union(set(tuple([(i,j)]))))
        self.trav(i-1, j, path.union(set(tuple([(i,j)]))))
        self.trav(i, j+1, path.union(set(tuple([(i,j)]))))
        self.trav(i, j-1, path.union(set(tuple([(i,j)]))))
