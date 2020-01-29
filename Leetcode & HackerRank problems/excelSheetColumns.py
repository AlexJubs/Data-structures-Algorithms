class Solution:
    def titleToNumber(self, s: str) -> int:
        words = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = 0
        c = 1
        for i in range(len(s)-1, -1, -1):
            res = res + words.index(s[i])*c
            c = c*26
        return res
