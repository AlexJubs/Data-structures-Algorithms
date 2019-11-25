class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = dict()
    
    def sumRange(self, i: int, j: int) -> int:
        if self.sums.get((i,j)) != None: return self.sums.get[i,j]
        return sum(self.nums[i:j+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)