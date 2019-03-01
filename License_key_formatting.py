class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = S.upper()
        S = S.replace('-','')
        output = ''
        temp = S[::-1]

        for i in range(len(S)):
            if (i%K == 0) and i != 0:
                output = output + '-'
            output = output + temp[i]

        output = output[::-1]

        return output
