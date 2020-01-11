class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.struct = dict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if self.struct.get(key) == None: self.struct[key] = 1
        else: self.struct[key] = self.struct[key] + 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if self.struct.get(key) == None: return
        self.struct[key] = self.struct[key] - 1
        if self.struct[key] == 0: del self.struct[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        maxKey = ("",-1)
        for x,y in self.struct.items():
            if y >= maxKey[1]: maxKey = (x,y)
        return maxKey[0]

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        minKey = ("",float('inf'))
        for x,y in self.struct.items():
            if y <= minKey[1]: minKey = (x,y)
        return minKey[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
