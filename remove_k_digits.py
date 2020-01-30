class Solution:
    def remover(self, num):
        res = 9999999999999
        for i in range(1,len(num)):
            res = min(res, int(num[:i]+ num[i+1:]))
        return str(res)
    
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'
        if k == 0: return num
        if num[1] == '0': return self.removeKdigits(num[2:],k-1)
        return self.removeKdigits(self.remover(num),k-1)