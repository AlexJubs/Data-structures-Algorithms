class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.words_arr = []
        self.lens = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words.add(word)
        self.words_arr.append(word)
        self.lens.add(len(word))
        

    def search(self, search: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(search) not in self.lens: return False
        if search in self.words: return True
        if '.' not in search: return search in self.words
        
        for x in self.words_arr:
            if len(x) != len(search): continue
            for i in range(len(x)):
                if i+1 != len(x):
                    if search[i] == '.': continue
                if search[i] != x[i] and search[i] != '.': break
                if i+1 == len(x): return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)