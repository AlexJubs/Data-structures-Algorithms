class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        x,y = bin(x)[2:], bin(y)[2:]
        if len(x) < len(y): x = (len(y)-len(x))*'0'+x
        if len(y) < len(x): y = (len(x)-len(y))*'0'+y
        for i in range(len(x)):
            if x[i] != y[i]: res=res+1
        return res
