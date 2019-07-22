"""
We can create a temp hashset and add numbers to it as we go. If we find a number which we've seen before, then we return false. If we traverse every row, every column and every 3x3 box we don't find a repeated number, then we return true.
We can create a helper function for each 3x3 box to return a bool
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkBox(x,y):
            S = set()
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if board[i][j] != '.':
                        if board[i][j] not in S:
                            S.add(board[i][j])
                        else:
                            return False
            return True
        
        def checkRow(y):
            S = set()
            for i in range(9):
                if board[i][y] != '.':
                    if board[i][y] not in S:
                        S.add(board[i][y])
                    else: 
                        return False
            return True
        
        def checkCol(x):
            S = set()
            for i in range(9):
                if board[x][i] != '.':
                    if board[x][i] not in S:
                        S.add(board[x][i])
                    else: 
                        return False
            return True
        
        if (checkBox(0,0) and checkBox(0,3) and checkBox(0,6) and checkBox(3,0) and checkBox(3,3) and checkBox(3,6) and checkBox(6,0) and checkBox(6,3) and checkBox(6,6)) == False: return False
        if (checkRow(0) and checkRow(1) and checkRow(2) and checkRow(3) and checkRow(4) and checkRow(5) and checkRow(6) and checkRow(7) and checkRow(8)) == False: return False
        if (checkCol(0) and checkCol(1) and checkCol(2) and checkCol(3) and checkCol(4) and checkCol(5) and checkCol(6) and checkCol(7) and checkCol(8)) == False: return False
        
        return True