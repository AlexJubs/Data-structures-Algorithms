class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (len(word) == 0 or len(word) == 1): return True
        Caps = set(           ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
        if word.upper() == word: return True
        if word.lower() == word: return True
        if word[0] in Caps:
            return word[1:] == word[1:].lower()