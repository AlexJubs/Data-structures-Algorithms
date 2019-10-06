class Solution:
    def populate(self, x, y, res):
        self.res = max(res,self.res)
        if (x+1 < self.w) and (self.grid[y][x+1] == 1):
            self.grid[y][x+1] = 2
            self.populate(x+1,y,res+1)
                  
        if (x-1 >= 0) and (self.grid[y][x-1] == 1):
            self.grid[y][x-1] = 2
            self.populate(x-1,y,res+1)
        
        if (y+1 < self.h) and (self.grid[y+1][x] == 1): 
            self.grid[y+1][x] = 2
            self.populate(x,y+1,res+1)
        
        if (y-1 >= 0) and (self.grid[y-1][x] == 1): 
            self.grid[y-1][x] = 2
            self.populate(x,y-1,res+1)
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.h = len(grid)
        self.w = len(grid[0])
        self.grid = grid
        self.res = 0
        coordinates = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    coordinates.append([x,y])
        for c in coordinates:
            self.populate(c[0],c[1],0)
            
        for a in self.grid:
            if 1 in a: return -1
            
        return self.res