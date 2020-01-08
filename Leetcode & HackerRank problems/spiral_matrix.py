class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1: return matrix[0]
        if len(matrix) == 0: return matrix
        self.res = list()
        self.matrix = matrix
        
        self.top_cuttoff = -1
        self.bottom_cuttoff = len(matrix)
        self.left_cuttoff = -1
        self.right_cuttoff = len(matrix[0])
        
        self.dfs(0,0,'right')
        return self.res
    
    def dfs(self, i, j, di):
        if i <= self.top_cuttoff or j <= self.left_cuttoff or j >= self.right_cuttoff or i >= self.bottom_cuttoff: return
        self.res.append(self.matrix[i][j])
        if di == 'right':
            self.dfs(i,j+1,'right')
            if j == self.right_cuttoff-1:
                self.top_cuttoff = self.top_cuttoff+1
                self.dfs(i+1, j, 'down')
                
        elif di == 'down':
            self.dfs(i+1, j, 'down')
            if i == self.bottom_cuttoff-1:
                self.right_cuttoff = self.right_cuttoff-1
                self.dfs(i, j-1, 'left')
                
        elif di == 'left':
            self.dfs(i, j-1, 'left')
            if j == self.left_cuttoff+1:
                self.bottom_cuttoff = self.bottom_cuttoff-1
                self.dfs(i-1, j, 'up')
                
        elif di == 'up':
            self.dfs(i-1, j, 'up')
            if i == self.top_cuttoff+1:
                self.left_cuttoff = self.left_cuttoff+1
                self.dfs(i, j+1, 'right')
