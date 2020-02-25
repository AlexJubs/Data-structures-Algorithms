class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stk = list()
        decomp = list()
        lower = -1
        for i in range(len(S)):
            if S[i] == '(': stk.append(S[i])
            elif S[i] == ')': stk.pop()
            
            if len(stk) == 0:
                decomp.append(S[lower+2:i])
                lower = i
        return ''.join(decomp)
