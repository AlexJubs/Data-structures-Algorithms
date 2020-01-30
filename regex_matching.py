class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = dict()
        return self.helper(s, p)
    
    def helper(self,s,p):
        if self.dp.get((s,p)) != None: return self.dp[(s,p)]
        if p == '.*': return True
        if '*' not in p and '.' not in p:
            self.dp[(s,p)] = (s == p)
            return s == p
            if p == '' or s == '': return False
        if p[0] == '*':
            self.dp[(s, p[1:])] = self.helper(s, p[1:])
            return self.helper(s, p[1:])
        if len(p) > 1 and p[1] == '*':
            for i in range(len(s)+1):
                if self.helper(s, p[0]*i + p[2:]) == True:
                    self.dp[(s, p[0]*i + p[2:])] = True
                    return True
        if len(s) > 0:
            if s[0] == p[0] or p[0] == '.':
                self.dp[(s,p)] = self.helper(s[1:], p[1:])
                return self.helper(s[1:], p[1:])
            if s[-1] == p[-1] or p[-1] == '.':
                self.dp[(s,p)] = self.helper(s[:-1], p[:-1])
                return self.helper(s[:-1], p[:-1])
        
        return False
