class Solution:
    def findInt(self, S: List[str]) -> int:
        res = 0
        S = S[::-1]
        for i in range(len(S)):
            if S[i] == '1':
                res = res + 2**i
        return res
    def findBinary(self, num: int) -> List[str]:
        if num == 1 or num == 0: return [str(num)]
        res = list('{0:0b}'.format(num))
        return res
    def findComplement(self, num: int) -> int:
        B = self.findBinary(num)
        for i in range(len(B)):
            if B[i] == '1': B[i] = '0'
            elif B[i] == '0': B[i] = '1'
        return self.findInt(B)