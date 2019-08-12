"""
We sort the array
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) < 3): return []
        res = []
        S = set()
        R = set()
        HashT = {}
        for x in nums:
            if x in S:
                HashT[x] = HashT[x]+1
            else:
                S.add(x)
                HashT[x] = 1
        if (0 in S and HashT[0] >= 3):
            res.append([0,0,0])
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                comp = -1*(nums[i]+nums[j])
                if comp in S:
                    if (comp == nums[i] or comp == nums[j]):
                        if HashT[comp] >= 2 and comp != 0:
                            temp = [nums[i],nums[j],comp]
                            temp.sort()
                            if (str(temp[0])+str(temp[1])+str(temp[2]) not in R):
                                R.add(str(temp[0])+str(temp[1])+str(temp[2]))
                                res.append(temp)
                    elif (comp != nums[i] and comp != nums[j]):
                        temp = [nums[i],nums[j],comp]
                        temp.sort()
                        if (str(temp[0])+str(temp[1])+str(temp[2]) not in R):
                            R.add(str(temp[0])+str(temp[1])+str(temp[2]))
                            res.append(temp)
        
        return res