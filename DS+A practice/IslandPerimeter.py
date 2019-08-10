"""
We want to find any 1 and then do a DFS on the 1 for all the neighbouring 1s. 
For each 1 that we find, we need to put its coordinates into a hashset so that we don't visit it again
For each 1 we traverse we need to count how many 0s are surrounding it, and add that number to res
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        trav = set()
        def dfs(x: int, y: int, res: int):
            trav.add(str(x)+'|'+str(y))
            if (x == 0 or grid[x-1][y] == 0): res=res+1;
            if (y+1 == len(grid[0]) or grid[x][y+1] == 0): res=res+1;
            if (x+1 == len(grid) or grid[x+1][y] == 0): res=res+1;
            if (y == 0 or grid[x][y-1] == 0): res=res+1;        
            
            if (x-1 >= 0 and grid[x-1][y] == 1 and str(x-1)+'|'+str(y) not in trav):
                res = dfs(x-1,y,res)
            if (x+1 < len(grid) and grid[x+1][y] == 1 and str(x+1)+'|'+str(y) not in trav):
                res = dfs(x+1,y,res)
            if (y-1 >= 0 and grid[x][y-1] == 1 and str(x)+'|'+str(y-1) not in trav):
                res = dfs(x,y-1,res)
            if (y+1 < len(grid[0]) and grid[x][y+1] == 1 and str(x)+'|'+str(y+1) not in trav):
                res = dfs(x,y+1, res)
            return res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    return dfs(i,j,0)
                    break
        return -1