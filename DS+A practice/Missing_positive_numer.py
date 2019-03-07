class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0) or (max(nums) <= 0) or (1 not in nums): return 1
        nums.sort()
        while max(nums) >= (2**31 - 5):
            nums.remove(max(nums))
            
        while min(nums) < 0:
            nums.remove(min(nums))
            
        for i in range(1,max(nums)):
            if i not in nums:
                return i
        return max(nums) +1