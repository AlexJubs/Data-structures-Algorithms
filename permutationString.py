from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        strs = list()
        self.C = Counter(s1)
        if len(s1) == len(s2): return self.isPermutation(s2)
        for i in range(len(s2)-len(s1)+1):
            strs.append(s2[i:i+len(s1)])
        for x in strs:
            if self.isPermutation(x): return True
        return False
    
    def isPermutation(self, s2):
        return self.C == Counter(s2)
