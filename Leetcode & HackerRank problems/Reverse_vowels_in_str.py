class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set(['a','o','e','i','u','A','E','I','O','U'])
        stk = list()
        s = list(s)
        for x in s:
            if x in v: stk.append(x)
        for i in range(len(s)):
            if s[i] in v: 
                s[i] = stk.pop()
        return ''.join(s)