class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        re_A, im_A = a.split('+')[0], a.split('+')[1][:-1] 
        re_B, im_B = b.split('+')[0], b.split('+')[1][:-1]
        real = int(re_A)*int(re_B) - int(im_A)*int(im_B)
        imaginary = int(re_A)*int(im_B) + int(im_A)*int(re_B)
        return str(real) + '+' + str(imaginary)+'i'