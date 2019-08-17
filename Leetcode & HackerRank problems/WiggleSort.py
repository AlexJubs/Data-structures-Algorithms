class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        if len(nums) < 2: return
        nums.sort()
        i = 2
        while (i < len(nums)-1):
            x = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = x
            i = i+2