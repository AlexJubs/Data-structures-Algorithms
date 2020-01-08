class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if t == s: return False
        if abs(len(s)-len(t)) > 1: return False
        if t == '': return len(s) <= 1
        if s == '': return len(t) <= 1
        if s[-1] == t[-1]: return self.isOneEditDistance(s[:-1], t[:-1])
        if s[0] == t[0]: return self.isOneEditDistance(s[1:], t[1:])
        if len(s) != len(t): return False
        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]: diff = diff+1
        return diff <= 1
