from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.struct = dict()
        for i in range(len(nums)):
            if self.struct.get(nums[i]) == None:
                self.struct[nums[i]] = (i,)
            else:
                self.struct[nums[i]] = self.struct[nums[i]] + (i,)

    def pick(self, target: int) -> int:
        if self.struct.get(target) == None: return 
        return self.struct[target][randint(0,len(self.struct[target])-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)