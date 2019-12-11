class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ind = dict()
        for i in range(len(arr2)): ind[arr2[i]] = i
        for x in arr1:
            if ind.get(x) == None: ind[x] = 2000 + x
        return sorted(arr1, key = lambda x: ind[x])

