# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inOrderTrav(self, root):
        if (root != None):
            self.inOrderTrav(root.left)
            self.nums.append(root.val)
            self.inOrderTrav(root.right)
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.nums = []
        self.inOrderTrav(root)
        h_set = set()
        for x in self.nums:
            if k-x in h_set: return True
            h_set.add(x)
        return False