class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.trav(word, i, j, set())
        return self.res
    
    def trav(self, rem, i, j, path):
        if (i,j) in path: return
        if self.res == True: return
        if rem == '':
            self.res = True
            return
        if i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0]): return
        if self.board[i][j] != rem[0]: return
        path.add((i,j))
        self.trav(rem[1:], i+1, j, path.union(set(tuple([(i,j)]))))
        self.trav(rem[1:], i-1, j, path.union(set(tuple([(i,j)]))))
        self.trav(rem[1:], i, j+1, path.union(set(tuple([(i,j)]))))
        self.trav(rem[1:], i, j-1, path.union(set(tuple([(i,j)]))))
