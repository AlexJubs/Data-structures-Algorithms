class Solution:
    def width(self, arr, ind):
        self.hash_set.add(tuple(ind))
        self.res = self.res + max(arr)-min(arr)

    def helper(self, arr, ind, p1):
        if arr != [] and tuple(ind) not in self.hash_set:
            self.width(arr, ind)
        
        if p1 >= len(self.A): return
        self.helper (arr + [self.A[p1]], ind + [p1],p1+1)
        self.helper (arr, ind, p1+1)
        
    def sumSubseqWidths(self, A):
        self.A = A
        self.hash_set = set()
        self.res = 0
        self.helper ([],[],0)
        return self.res
