# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def path(self, root, path_sum):
        if root == None: return
        if path_sum + root.val == self.target_sum: self.res = self.res +1
        self.path (root.left, path_sum + root.val)
        self.path (root.right, path_sum + root.val)
        
    def pathSum(self, root: TreeNode, s: int) -> int:
        if root == None: return 0
        self.target_sum = s
        self.res = 0
        self.start_sum(root)
        return self.res

    def start_sum(self, root):
        if root == None: return
        self.path(root, 0)
        self.start_sum(root.left)
        self.start_sum(root.right)
