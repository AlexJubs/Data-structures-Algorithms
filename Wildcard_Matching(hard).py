class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_a = ''
        i = 0
        self.dp = dict()
        while i < len(p):
            if p[i] != '*':
                p_a = p_a + p[i]
                i = i+1
                continue
            elif p[i] == '*':
                p_a = p_a + '*'
                while p[i] == '*':
                    i = i+1
                    if i >= len(p): break
        return self.helper(s, p_a)
    
    def helper(self, s, p):
        if self.dp.get((s,p)) != None: return self.dp[(s,p)]
        if '*' not in p and '?' not in p:
            self.dp[(s,p)] = p == s
            return p == s
        if '*' not in p and len(p) != len(s):
            self.dp[(s,p)] = False
            return False
        if p == '*':
            self.dp[(s,p)] = True
            return True
        if p == '' or s == '':
            self.dp[(s,p)] = False
            return False
        if s[0] == p[0] or p[0] == '?':
            self.dp[(s,p)] = self.helper(s[1:], p[1:])
            return self.dp[(s,p)]
        if s[-1] == p[-1] or p[-1] == '?':
            self.dp[(s,p)] = self.helper(s[:-1], p[:-1])
            return self.dp[(s,p)]
        if p[0] != '*' or p[-1] != '*':
            self.dp[(s,p)] = False
            return False
        if p[0] == '*':
            for i in range(len(s)):
                if self.helper(s[i:], p[1:]) == True:
                    self.dp[(s,p)] = True
                    return True
                
        self.dp[(s,p)] = False
        return False
