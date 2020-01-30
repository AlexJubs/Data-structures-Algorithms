class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        for i in range(0,len(nums)+1):
            for j in range(i,len(nums)+1):
                temp = nums[i:j]
                sumb = 0
                for p in range(0,len(temp)):
                    sumb = sumb + temp[p]

                if (sumb == k) and (len(temp) != 0):
                    counter = counter+1

        return counter