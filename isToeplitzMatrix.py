"""
traverse the diagonals, number of diagonals is M+N-1
"""
class Solution:
    def checkDiag(self, i, j):
        val = self.matrix[i][j]
        while (i < len(self.matrix) and j < len(self.matrix[0])):
            if self.matrix[i][j] != val: return False
            i = i+1
            j = j+1
        return True
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if matrix == []: return True
        self.matrix = matrix
        m, n = len(matrix[0]), len(matrix)
        for i in range(n):
            if self.checkDiag(i,0) == False: return False
        for i in range(1,m):
            if self.checkDiag(0,i) == False: return False
        return True
