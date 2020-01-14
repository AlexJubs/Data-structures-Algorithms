class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if A == []: return A
        res = list()
        for i in range(len(A[0])): res.append([-1]*len(A))
        for i in range(len(A)):
            for j in range(len(A[0])):
                res[j][i] = A[i][j]
        return res
