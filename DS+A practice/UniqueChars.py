"""
traverse the string and keep a hashset of all the seen characters. Everytime we traverse, we check if we've seen it before. if we reach the end of the string we return -1
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if (len(s) == 1): return 0
        HashT = {}
        for i in range(len(s)):
            if s[i] not in HashT:
                HashT[s[i]] = 1
            else:
                HashT[s[i]] = HashT[s[i]] + 1
        for i in range(len(s)):
            if (HashT[s[i]] == 1): return i
        return -1