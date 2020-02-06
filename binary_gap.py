class Solution:
    def binaryGap(self, N: int) -> int:
        b = list(bin(N)[2:])
        if b.count ('1') == 1: return 0
        while b[-1] == '0': b.pop()
        i = 0
        res = 1
        temp = 1
        while i < len(b):
            if b[i] == '1':
                temp = 1
            if b[i] == '0':
                temp = temp+1
            res = max(res,temp)
            i = i+1
        return res
