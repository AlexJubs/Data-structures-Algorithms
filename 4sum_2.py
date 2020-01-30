from collections import defaultdict
class Solution: 
    def getcomb(self, nums, res, lst1, lst2):
        for r in lst2:
            for l in lst1:    
                if l[0] not in r and l[1] not in r and nums[l[0]] <= nums[r[0]] <= nums[l[1]] <= nums[r[1]]: 
                    # Make sure no number can be used twice and avoid duplicate
                    comb = (  nums[l[0]], nums[l[1]], nums[r[0]], nums[r[1]]  )
                    if comb not in res:
                        res.add(comb)
        return
                    
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4 or len(nums) == 4 and sum(nums) != target:
            return []
       
        nums.sort() # Sorting for easy duplicate detection
        my_dict = defaultdict(list)
        for r in range(1, len(nums)):
            for l in range(r): # Set rule to let r must be larger than l to avoid repeating
                my_dict[nums[l]+nums[r]].append((l,r)) # Use index instead of value to make sure no number can be used twice
        
        res = set()
        for k, v in my_dict.items():
            lookfor = target - k
            if lookfor > k and lookfor in my_dict:  # Set rule to let 1st two-sum must be larger than 2nd two-sum to avoid repeating
                self.getcomb(nums, res, v, my_dict[lookfor])
            elif lookfor == k: # If k == target//2, build combination from current two-sum list
                self.getcomb(nums, res, v, v)

        return res
