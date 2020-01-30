class Solution:
    def buildSum (self, arr, p1, s):
        if s == self.target: self.res.add(tuple(arr))
        if s > self.target: return
        if p1 >= len(self.candidates): return
        self.buildSum(arr, p1+1, s)
        self.buildSum(arr+ [self.candidates[p1]], p1+1, s+self.candidates[p1])
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []: return []
        self.candidates = sorted(candidates)
        self.target = target
        self.res = set()
        self.buildSum([], 0, 0)
        
        return list(self.res)
