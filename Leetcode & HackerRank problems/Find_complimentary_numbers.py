class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        res = []
        S = set(nums)
        comp =  [i for i in range(1,len(nums)+1)]
        for x in comp:
            if x not in S: res.append(x)
        return res