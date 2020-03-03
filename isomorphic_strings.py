class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_t = dict()
        values = set()
        if len(s) == 0 and len(t) == 0: return True
        if len(s) != len(t): return False
        for i in range(len(s)):
            if hash_t.get(s[i]) == None:
                if t[i] in values: return False
                hash_t[s[i]] = t[i]
                values.add(t[i])
            else:
                if hash_t[s[i]] != t[i]: return False
        return True
