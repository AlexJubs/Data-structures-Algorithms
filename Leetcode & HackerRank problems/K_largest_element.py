class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == len(nums): return min(nums)
        if k == 1: return max(nums)
        nums.sort()
        nums = nums[::-1]
        return nums[k-1]
