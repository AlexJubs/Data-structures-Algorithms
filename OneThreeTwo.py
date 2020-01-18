class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = -1*float('inf')
        stk = list()
        for i in range(len(nums)-1,-1,-1):
            if third > nums[i]: return True
            else:
                while len(stk) != 0 and nums[i] > stk[-1]:
                    third = stk.pop()
            stk.append(nums[i])
        return False
