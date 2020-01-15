class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        path = path.split('/')
        for x in path:
            if x == '' or x == '.': continue
            if x == '..':
                if len(stk) != 0: stk.pop()
                continue
            stk.append(x)
        if stk:
            res = '/'
            for x in stk: res = res + x + '/'
            return res[:-1]
        else: return '/'
