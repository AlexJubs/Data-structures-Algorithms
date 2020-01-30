class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq = dict()
        for x in A:
            if freq.get(x) == None: freq[x] = 0
            freq[x] = freq[x] +1
        res = -1
        for x,y in freq.items():
            if y == 1: res = max(res, x)
        return res
