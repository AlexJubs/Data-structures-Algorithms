from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        for x in ransomNote:
            if letters.get(x) == None: return False
            letters[x] = letters[x]-1
            if letters[x] < 0: return False
        return True
