class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ind = set()
        stk = list()
        for i in range(len(s)):
            if s[i] == '(': stk.append(s[i])
            if s[i] == ')':
                if len(stk) == 0: ind.add(i)
                elif len(stk) > 0: stk.pop()
        
        if len(stk) == 0:
            res = ''
            for i in range(len(s)):
                if i not in ind: res = res + s[i]
            return res
        if len(stk) > 0:
            for i in range(len(s)-1,-1,-1):
                if s[i] == '(':
                    ind.add(i)
                    stk.pop()
                if len(stk) == 0: break
            res = ''
            for i in range(len(s)):
                if i not in ind: res = res + s[i]
            return res