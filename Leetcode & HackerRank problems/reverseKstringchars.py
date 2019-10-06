class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        i = 0
        while i < len(s):
            if (i+k < len(s)): sub = s[i:i+k][::-1]
            else: sub = s[i:len(s)][::-1]
            if (i+2*k >= len(s)): rem = s[i+k:len(s)]
            else: rem = s[i+k:i+2*k]
            res = res + sub + rem
            i = i+2*k
        return res