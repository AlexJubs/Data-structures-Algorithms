class Solution:
    def maxAreaOfIsland(self, Matrix: List[List[int]]) -> int:
        def dfs(x: int, y: int, Num: int) -> int:
            Matrix[x][y] = 0
            if (x-1 >= 0) and (Matrix[x-1][y] == 1): Num = dfs(x-1, y, Num+1)
            if (x+1 < len(Matrix)) and (Matrix[x+1][y] == 1): Num = dfs(x+1, y, Num+1)
            if (y-1 >= 0) and (Matrix[x][y-1] == 1): Num = dfs(x, y-1, Num+1)
            if (y+1 < len(Matrix[0])) and (Matrix[x][y+1] == 1): Num = dfs(x, y+1, Num+1)
            
            return Num
        
        res = 0
        for i in range(len(Matrix)):
            for j in range(len(Matrix[0])):
                if (Matrix[i][j] == 1):
                    Matrix[i][j] = 0
                    res = max(dfs(i,j, 1),res)
        return res

    
