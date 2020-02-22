class Solution:
    def trav(self, arr, s_arr):
        if len(arr) == len(self.nums):
            self.res.append(arr)
            return
        for x in self.nums:
            if x not in s_arr:
                self.trav(arr + [x], s_arr|set([x]))
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = list()
        self.trav(list(), set())
        return self.res
