class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (s == '') or (len(s) == 1): return s
        ans = []
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                if (i!=j) and (s[i:j] != ''):
                    str1 = s[i:j]
                    str2 = str1[::-1]
                    if (str1 == str2):
                        ans.append(str2)
        max_ = 0
        for i in range(len(ans)):
            if (len(ans[i])>len(ans[max_])):
                max_ = i
        return ans[max_]