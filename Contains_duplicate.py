"""
add nums[i] to a hashset as we go, and create a hashmap to map nums->index. Once we encounter some nums[i] which is already in the set, we check its index on the hashmap. if cur-i <= k then we return true, otherwise we replace hashmap[nums] to the new index. if we traverse the full array, return false
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        S = set()
        Map = {}
        for i in range(len(nums)):
            if nums[i] not in S:
                Map[nums[i]] = i
                S.add(nums[i])
            else:
                if (i-Map[nums[i]] <= k):
                    return True
                Map[nums[i]] = i
        return False