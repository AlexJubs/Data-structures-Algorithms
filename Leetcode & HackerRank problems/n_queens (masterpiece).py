class Solution:
    def solveNQueens(self, n):
        self.d = n
        board = list()
        for i in range(n):
            row = list()
            for j in range(n):
                row.append('.')
            board.append(row)
        self.res = list()
        self.helper(n,board,0)
        return self.res
        
    def helper(self, n, board, pos):      
        if n == 0:
            temp = list()
            for x in board:
                temp.append(''.join(x))
            self.res.append(temp)
            return
        if pos > self.d*self.d -1: return
        i = int (pos / self.d)
        j = int (pos % self.d)
        if n == self.d or (self.ValidRow(board,i) and self.ValidCol(board,j) and self.ValidDiag(board,i,j)):
            board[i][j] = 'Q'
            self.helper(n-1, board, pos+1)
        board[i][j] = '.'
        self.helper(n,board, pos+1)
        
    def ValidRow(self, board, row):
        return 'Q' not in board[row]
    
    def ValidCol(self, board, col):
        for i in range(self.d):
            if board[i][col] == 'Q': return False
        return True
    
    def ValidDiag(self, board, row, col):
        tmp_row = row
        tmp_col = col
        while (tmp_row < self.d and tmp_col < self.d):
            if board[tmp_row][tmp_col] == 'Q': return False
            tmp_row = tmp_row+1
            tmp_col = tmp_col+1
        tmp_row = row
        tmp_col = col
        while (tmp_row >= 0 and tmp_col < self.d):
            if board[tmp_row][tmp_col] == 'Q': return False
            tmp_row = tmp_row-1
            tmp_col = tmp_col+1
        tmp_row = row
        tmp_col = col
        while (tmp_row < self.d and tmp_col >= 0):
            if board[tmp_row][tmp_col] == 'Q': return False
            tmp_row = tmp_row+1
            tmp_col = tmp_col-1
        tmp_row = row
        tmp_col = col
        while (tmp_row >= 0 and tmp_col >= 0):
            if board[tmp_row][tmp_col] == 'Q': return False
            tmp_row = tmp_row-1
            tmp_col = tmp_col-1
        return True

