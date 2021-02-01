class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or s == "": return 0
        buffer = dict()
        p1 = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in buffer: buffer[s[i]] = 0
            buffer[s[i]] += 1
            
            while(len(buffer) > k):
                if buffer[s[p1]] > 1: buffer[s[p1]] -= 1
                else: del buffer[s[p1]]
                p1 += 1
                
            res = max(res, i-p1+1)
        return res
