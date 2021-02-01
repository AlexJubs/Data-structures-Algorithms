from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = Counter(s1)
        n = len(s1)
        window = Counter(s2[:n])
        if window == f1: return True
        p1 = 0
        p2 = n
        while p2 < len(s2):
            if s2[p2] not in window: window[s2[p2]] = 0
            window[s2[p2]] += 1
            if window[s2[p1]] > 1: window[s2[p1]] -= 1
            else: del window[s2[p1]]
            if window == f1: return True
            p1 += 1
            p2 += 1
            
        return False
