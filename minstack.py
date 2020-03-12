class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = list()
        self.minimums = list()

    def push(self, x: int) -> None:
        self.stk.append(x)
        if len(self.minimums) == 0 or self.minimums[-1] >= x:
            self.minimums.append(x)

    def pop(self) -> None:
        x = self.stk.pop()
        if x == self.minimums[-1]:
            self.minimums.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
