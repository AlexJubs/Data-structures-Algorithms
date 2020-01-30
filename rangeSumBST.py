# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None: return 0
        if root.val >= L and root.val <= R: to_add = root.val
        else: to_add = 0
        return to_add + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)
