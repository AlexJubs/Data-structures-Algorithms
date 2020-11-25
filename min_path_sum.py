class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0
        if len(grid) == 1: return grid[0][0]
        dp = [[-1]*len(grid[0])]*len(grid)
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if (i == len(grid)-1 and j == len(grid[0])-1):
                    dp[i][j] = grid[i][j]
                    
                if (i == len(grid)-1 and j != len(grid[0])-1):
                    dp[i][j] = dp[i][j+1] + grid[i][j]
                if (i != len(grid)-1 and j== len(grid[0])-1):
                    dp[i][j] = dp[i+1][j] + grid[i][j]

                if (i != len(grid)-1 and j != len(grid[0])-1):
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        return dp[0][0]
