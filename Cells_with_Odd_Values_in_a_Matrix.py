class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odd_count = 0
        rows = [0] * n
        cols = [0] * m

        for i, j in indices:
            rows[i] = rows[i] ^ 1
            cols[j] = cols[j] ^ 1

        for i in range(n):
            for j in range(m):
                if(rows[i] ^ cols[j] == 1): odd_count += 1

        return odd_count
