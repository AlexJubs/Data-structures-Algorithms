class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum_matrix = list()
        buffer = list()
        for x in matrix:
            buffer = [x[0]]
            for k in range(1,len(x)):
                buffer.append(x[k]+buffer[-1])
            self.prefix_sum_matrix.append(buffer)
        print(self.prefix_sum_matrix)
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for k in range(row1, row2+1):            
            res += self.prefix_sum_matrix[k][col2]
            if col1 != 0: res -= self.prefix_sum_matrix[k][col1-1]
        return res
