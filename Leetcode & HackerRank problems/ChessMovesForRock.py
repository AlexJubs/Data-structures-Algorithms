class Solution:
    def checkUp(self, y, x):
        if y < 0: return True
        if self.grid[y][x] == 'p': return False
        if self.grid[y][x] == 'B': return True
        return self.checkUp(y-1,x)
    
    def checkDown(self, y, x):
        if y >= len(self.grid): return True
        if self.grid[y][x] == 'p': return False
        if self.grid[y][x] == 'B': return True
        return self.checkDown(y+1,x)
        
    def checkRight(self, y, x):
        if x >= len(self.grid[0]): return True
        if self.grid[y][x] == 'p': return False
        if self.grid[y][x] == 'B': return True
        return self.checkRight(y,x+1)
    
    def checkLeft(self, y, x):
        if x < 0: return True
        if self.grid[y][x] == 'p': return False
        if self.grid[y][x] == 'B': return True
        return self.checkLeft(y,x-1)
            
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        self.grid = board
        checked = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    if self.checkUp(i,j): res = res +1
                    if self.checkRight(i,j): res = res +1
                    if self.checkLeft(i,j): res = res +1
                    if self.checkDown(i,j): res = res +1
                    checked = True
                if checked: break
            if checked: break
        return 4-res