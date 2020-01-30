class Solution:
    def flip(self, x):
        if x == 1: return 0
        if x == 0: return 1
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = A[i][::-1]
            A[i] = list(map(self.flip,A[i]))
        return A