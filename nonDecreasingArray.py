"""
find the first instance of a decreasing element, modify the leftmost element to be rightmost-1, return true if the new array is non-decreasing
"""
class Solution:
    def isIncreasing(self, nums):
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]: return False
        return True
    def checkPossibility(self, nums: List[int]) -> bool:
        if self.isIncreasing(nums): return True
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return self.isIncreasing(nums[:i]+nums[i+1:]) or self.isIncreasing(nums[:i+1]+nums[i+2:])

