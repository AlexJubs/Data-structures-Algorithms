class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        p1 = p2 = 0
        while (p1 < len(A) and p2 < len(B)):
            # if they intersect, add them
            if (A[p1][1] < B[p2][0] or B[p2][1] < A[p1][0]) == False:
                lower = max(A[p1][0], B[p2][0])
                upper = min(A[p1][1], B[p2][1])
                res.append([lower, upper])
            # if move the one with the smaller upper bound up
            if (A[p1][1] < B[p2][1]): p1 =p1+1
            else: p2 = p2+1
        return res