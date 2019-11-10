class WordDistance:

    def __init__(self, words: List[str]):
        self.vocab = dict()
        for i in range(len(words)):
            if self.vocab.get(words[i]) == None: self.vocab[words[i]] = (i)
            else:
                if isinstance(self.vocab[words[i]], tuple):
                    self.vocab[words[i]] = self.vocab[words[i]] + (i,)
                else: self.vocab[words[i]] = (self.vocab[words[i]],) + (i,)
        
    def shortest(self, word1: str, word2: str) -> int:
        if isinstance(self.vocab[word1], tuple): arr_1 = list(self.vocab[word1])
        else: arr_1 = [self.vocab[word1]]

        if isinstance(self.vocab[word2], tuple): arr_2 = list(self.vocab[word2])
        else: arr_2 = [self.vocab[word2]]
        
        res = float('inf')
        for x in arr_1:
            for y in arr_2:
                res = min(res,abs(x-y))
        return res
    
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)