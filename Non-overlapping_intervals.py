class Solution:
    def overlaps(self, A, B):
        return max(A[0],B[0]) < min(A[1],B[1])
        
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []: return 0
        res = 0
        intervals.sort(key=lambda i: i[1])
        prev = intervals[0]
        for i in range(1,len(intervals)):
            if self.overlaps(intervals[i], prev): res = res+1
            else: prev = intervals[i]
        return res
