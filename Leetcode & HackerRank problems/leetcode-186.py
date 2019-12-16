"""
2 pointers - move p2 up until it hits a space, then perform reverse algo, then let p1 = p2 and repeat
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        upper, lower = len(s)-1, 0
        while (upper > lower):
            s[upper], s[lower] = s[lower], s[upper]
            upper = upper-1
            lower = lower+1
            
        p2 = p1 = 0
        while p2 < len(s):
            if s[p2] == ' ' or p2+1 == len(s):
                # reverse
                upper, lower = p2-1, p1
                if p2+1 == len(s): upper = p2
                while (upper > lower):
                    s[upper], s[lower] = s[lower], s[upper]
                    upper = upper-1
                    lower = lower+1
                p1 = p2+1
            p2 = p2+1
