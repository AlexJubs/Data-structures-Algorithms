class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_array = nums1 + nums2
        new_array.sort()
        
        if (len(new_array)%2 == 1):
            return(new_array[len(new_array)/2])
        
        elif (len(new_array)%2 == 0):
            upper = (len(new_array)/2)
            lower = (len(new_array)/2)-1
            
            return float(new_array[upper]+new_array[lower])/2