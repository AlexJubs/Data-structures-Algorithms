'''
[-4,-1,1,2]
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        i = 0
        while (True):
            if (self.threeSum(nums, target+i)): return target+i
            if (self.threeSum(nums, target-i)): return target-i
            i += 1
        
        return target
            
    def threeSum(self, nums, target):
        indicies = dict()
        for i in range(len(nums)):
            indicies[nums[i]] = i
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (target - (nums[i]+nums[j]) in indicies) and (indicies[target - (nums[i]+nums[j])] not in {i,j}):
                    return True
                
        return False
