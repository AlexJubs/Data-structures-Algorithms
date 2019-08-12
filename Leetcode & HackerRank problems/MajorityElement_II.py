class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        key = len(nums)/3
        output = []
        nums.sort()
        i = 0
        while (i < len(nums)):
            if (nums.count(nums[i]) > key and nums[i] not in output):
                output.append(nums[i])
            i = i + nums.count(nums[i])
        return output