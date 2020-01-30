# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.arr = []
        self.inOrderTrav(root)

    def inOrderTrav(self, root):
        if root != None:
            self.inOrderTrav(root.left)
            self.arr.append(root.val)
            self.inOrderTrav(root.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.arr.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.arr) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()