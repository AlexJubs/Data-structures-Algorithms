class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if (len(nums) == 3): return nums[0]*nums[1]*nums[2]
        nums.sort()
        l = len(nums)
        if (nums[0] >= 0): return nums[l-1]*nums[l-2]*nums[l-3]
        a = nums[l-1]*nums[l-2]*nums[l-3]
        b = nums[0]*nums[1]*nums[2]
        c = nums[0]*nums[l-1]*nums[l-2]
        d = nums[0]*nums[1]*nums[l-1]
        return max(max(a,b),max(c,d))