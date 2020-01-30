class Solution:
    def helper(self, s, p1):
        if p1 == self.limit:
            self.res.append(s)
            return
        for x in self.phone[self.digits[p1]]:
            self.helper(s + x, p1+1)
        
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        self.digits = digits
        self.phone = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wyxz"}
        self.limit = len(digits)
        self.res = list()
        self.helper('',0)
        return self.res