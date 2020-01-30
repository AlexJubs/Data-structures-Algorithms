class Solution:
    def isValid(self, s: str) -> bool:
        B = set(['[','{','('])
        stack = []
        for x in s:
            if x in B:
                stack.append(x)
            else:
                if len(stack) == 0: return False
                elif x == ')' and stack[-1] != '(': return False
                elif x == '}' and stack[-1] != '{': return False
                elif x == ']' and stack[-1] != '[': return False
                else: stack.pop()
        return len(stack) == 0