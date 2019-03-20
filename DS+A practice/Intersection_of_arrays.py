class Solution(object):
    def intersect(self, nums1, nums2):
        if (len(nums1) > len(nums2)):
            nums1, nums2 = nums2, nums1
        if (len(nums1) == 0 or len(nums2) == 0): return []
        output = []
        for i in range(len(nums1)):
            if (nums1[i] in nums2 and nums1[i] not in output):
                for k in range(min(nums2.count(nums1[i]), nums1.count(nums1[i]))):
                    output.append(nums1[i])
        output.sort()
        return output