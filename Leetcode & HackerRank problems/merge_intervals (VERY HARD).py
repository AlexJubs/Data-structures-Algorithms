class Solution:
    def intersects(self, A, B):
        if A == B: return True
        if (A[0] <= B[1] and A[0] >= B[0]) or (A[1] >= B[0] and A[1] <= B[1]) or (A[0] <= B[0] and A[1] >= B[1]): return True
        else: return False
     
    def dummyMerge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1: return intervals
        res = []
        intervals.sort()
        lower = upper = 0
        openInterval = False

        while (upper+1 < len(intervals)):
            if (self.intersects(intervals[lower],intervals[upper+1])):
                upper = upper+1
                openInterval = True
                continue
                
            res.append([min(intervals[lower][0],intervals[upper][0]),
                        max(intervals[upper][1],intervals[lower][1])])
            openInterval = False
            lower = upper = upper+1
            
        if openInterval:
            res.append([min(intervals[lower][0],intervals[upper][0]),
                        max(intervals[upper][1],intervals[lower][1])])
            
        if res[-1][1] != max(self.hash_s):
            if self.intersects(intervals[upper],res[-1]):
                    res[-1] = [min(res[-1][0],intervals[upper][0]),
                               max(intervals[upper][1], res[-1][1])]
                    
            else: res.append(intervals[upper])

        return res
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1: return intervals
        res = []
        intervals.sort()
        lower = upper = 0
        openInterval = False

        new_intervals = []
        self.hash_s = set()
        for i in range(len(intervals)):
            if intervals[i][0] == intervals[i][1] and intervals[i][0] in self.hash_s: continue
            else:
                new_intervals.append(intervals[i])
                self.hash_s.add(intervals[i][0])
                self.hash_s.add(intervals[i][1])
                
        if (len(new_intervals) == 1): return new_intervals
        
        intervals = new_intervals

        while (upper+1 < len(intervals)):
            if (self.intersects(intervals[lower],intervals[upper+1])):
                upper = upper+1
                openInterval = True
                continue
                
            res.append([min(intervals[lower][0],intervals[upper][0]),
                        max(intervals[upper][1],intervals[lower][1])])
            openInterval = False
            lower = upper = upper+1
            
        if openInterval:
            res.append([min(intervals[lower][0],intervals[upper][0]),
                        max(intervals[upper][1],intervals[lower][1])])
            
        if res[-1][1] != max(self.hash_s):
            if self.intersects(intervals[upper],res[-1]):
                    res[-1] = [min(res[-1][0],intervals[upper][0]),
                               max(intervals[upper][1], res[-1][1])]
                    
            else: res.append(intervals[upper])

        while (len(res) != len(self.dummyMerge(res))): res = self.dummyMerge(res)
        return res