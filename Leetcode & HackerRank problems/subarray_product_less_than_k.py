class Solution:
    def product(self, nums):
        res = 1
        for x in nums: res = res*x
        return res
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p1 = p2 = res = 0
        while (p1 < len(nums)):
            while (p2 < len(nums)):
                #print (nums[p1:p2+1])
                if self.product(nums[p1:p2+1]) < k:
                    res = res +1
                p2 = p2+1
            p2 = p1+1
            p1 = p1+1
        return res