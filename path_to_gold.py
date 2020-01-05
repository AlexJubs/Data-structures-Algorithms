class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.grid = grid
        self.dp = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.trav(i, j, set(), 0)
        return self.res
        
    def trav(self, i, j, path, gold):
        self.res = max(self.res, gold)
        if (i,j) in path: return
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] == 0:
            return
        path.add((i,j))
        self.trav(i+1, j, path, gold+self.grid[i][j])
        path.remove((i,j))
        path.add((i,j))
        self.trav(i-1, j, path, gold+self.grid[i][j])
        path.remove((i,j))
        path.add((i,j))
        self.trav(i, j+1, path, gold+self.grid[i][j])
        path.remove((i,j))
        path.add((i,j))
        self.trav(i, j-1, path, gold+self.grid[i][j])
        path.remove((i,j))
