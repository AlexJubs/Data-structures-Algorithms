class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_t = dict()
        S = set()
        for x in arr:
            if hash_t.get(x) != None: hash_t[x] = hash_t[x] + 1
            else: hash_t[x] = 0
        for value in hash_t.values():
            if value in S: return False
            S.add(value)
        return True