# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None: return t2
        if t2 == None: return t1
        if t1.left == None and t1.right == None:
            t2.val = t2.val + t1.val
            return t2
        if t2.left == None and t2.right == None:
            t1.val = t1.val + t2.val
            return t1
        root = ListNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root
