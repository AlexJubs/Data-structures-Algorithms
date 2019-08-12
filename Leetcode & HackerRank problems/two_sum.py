class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return_array = []
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if (nums[i]+nums[j] == target) and (i != j):
                    return_array.append(i)
                    return_array.append(j)
                    return (return_array)
                