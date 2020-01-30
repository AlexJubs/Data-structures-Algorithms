class Solution:
    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            self.arr.append(root.val)
            self.inOrder(root.right)
            
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.arr = []
        self.inOrder(root)
        res = 9999999
        for i in range(len(self.arr)-1): res = min(res, self.arr[i+1] - self.arr[i])
        return res
