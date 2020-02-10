class Solution:
    def checkWinner(self):
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] and self.grid[1][i] == self.grid[2][i]:
                return self.grid[1][i]
            elif self.grid[i][0] == self.grid[i][1] and self.grid[i][1] == self.grid[i][2]:
                return self.grid[i][1]
        if self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]: return self.grid[1][1]
        if self.grid[2][0] == self.grid[1][1] and self.grid[1][1] == self.grid[0][2]: return self.grid[1][1]
        return 'Pending'
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5: return 'Pending'
        self.grid = [['.',',',']'],['[','=','2'],['4','1','g']]
        c = 0
        for x in moves:
            if c%2 == 0: self.grid[x[0]][x[1]] = 'A'
            elif c%2 == 1: self.grid[x[0]][x[1]] ='B'
            c = c+1
        if self.checkWinner() in {'A','B'}: return self.checkWinner()
        if len(moves) != 9: return 'Pending'
        return 'Draw'
        
