class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.endofword = False
    
class Trie(TrieNode):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("root")
        
    def insert_helper(self, head, word, p1):
        if p1 >= len(word):
            head.endofword = True
            return
        if word[p1] in head.children:
            self.insert_helper(head.children[word[p1]], word, p1+1)
        else:
            head.children[word[p1]] = TrieNode(word[p1])
            self.insert_helper(head.children[word[p1]], word, p1+1)
        
    def search_helper(self, head, word, p1):
        if p1 >= len(word):
            return head.endofword
        if word[p1] in head.children:
            return self.search_helper(head.children[word[p1]], word, p1+1)
        return False
    
    def startsWith_helper(self, head, word, p1):
        if p1 >= len(word):
            return True
        if word[p1] in head.children:
            return self.search_helper(head.children[word[p1]], word, p1+1)
        return False
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.insert_helper(self.root, word, 0)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        self.search_helper(self.root, word, 0)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        self.startsWith_helper(self.root, prefix, 0) 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
