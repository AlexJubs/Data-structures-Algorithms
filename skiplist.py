class Skiplist:

    def __init__(self):
        self.structure = dict()

    def search(self, target: int) -> bool:
        if self.structure.get(target) == None: return False
        return self.structure[target] > 0

    def add(self, num: int) -> None:
        if self.structure.get(num) != None:
            self.structure[num] = self.structure[num] + 1
        else: 
            self.structure[num] = 1

    def erase(self, num: int) -> bool:
        if self.structure.get(num) == None: return False 
        elif self.structure[num] == 0: return False
        self.structure[num] = self.structure[num] - 1
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
