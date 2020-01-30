class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        self.index = dict()
        for i in range(len(keyboard)): self.index[keyboard[i]] = i 
        if len(word) == 1: return self.index[word]
        p1 = 0
        res = 0
        for x in word:
            res = res + abs(p1-self.index[x])
            p1 = self.index[x]
        return res