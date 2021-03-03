class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2: return []
        HashT = defaultdict(list)
        res = set()
        for i in range(len(nums)): HashT[nums[i]].append(i)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                third_num = -1*(nums[i]+nums[j])
                if tuple(sorted((nums[i], nums[j], third_num))) in res: continue
                if third_num in HashT:
                    for third in HashT[third_num]:
                        if third != i and third != j:
                            res.add(tuple(sorted((nums[i], nums[j], third_num))))
        return list(map(lambda x: list(x), list(res)))
