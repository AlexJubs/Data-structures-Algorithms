class Solution:
    def trav(self, arr, s_arr):
        if len(arr) == len(self.nums):
            self.res.add(arr)
            return
        for i in range(len(self.nums)):
            if i not in s_arr:
                self.trav(arr + tuple([self.nums[i]]), s_arr|set([i]))
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = set()
        self.trav(tuple([]), set())
        return list(self.res)
