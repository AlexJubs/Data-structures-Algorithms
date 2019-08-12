class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1: return num
        else:
            nums = list(str(num))
            num = 0
            for x in nums:
                num = num+int(x)
            return self.addDigits(num)