class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        alph = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        string = ''
        for c in S:
            if c in alph:
                string = c + string
        p1 = 0
        for i in range(len(S)):
            if S[i] in alph:
                S[i] = string[p1]
                p1 = p1+1
        return ''.join(S)
