class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        if ("abc" not in S): return False
        a = S
        while (a != ''):
            if ('abc' not in a): return False
            a = a.split("abc")
            a = ''.join(a)
            
        return True