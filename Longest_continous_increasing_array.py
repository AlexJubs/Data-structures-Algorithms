class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []: return 0
        res = 1
        temp = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                temp = temp+1
            else: temp = 1
            res = max(res,temp)
        return res