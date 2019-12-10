class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2+1):
            pat = s[:i]
            if len(s)%len(pat) != 0: continue
            if pat*int(len(s)/len(pat)) == s: return True
        return False
