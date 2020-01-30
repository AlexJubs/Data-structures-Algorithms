class Solution:
    def divides(self, A, B):
        return B*int(len(A)/len(B)) == A
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2: return str2
        if len(str1) <= len(str2): B = str1
        else: B = str2
        res = ""
        for i in range(len(B),0,-1):
            if (self.divides(str1,B[:i]) and self.divides(str2,B[:i])):
                 return(B[:i])
        return res