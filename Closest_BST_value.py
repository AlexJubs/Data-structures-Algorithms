# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inOrderTrav(self, root):
        if root != None:
            self.inOrderTrav(root.left)
            self.arr.append(root.val)
            self.inOrderTrav(root.right)
    def closestValue(self, root: TreeNode, target: float):
        self.arr = list()
        self.inOrderTrav(root)
        res = list()
        delta = float('inf')
        for i in range(len(self.arr)):
            if abs(target-self.arr[i]) < delta:
                delta = abs(target-self.arr[i])
                middle = i
        return self.arr[middle]
