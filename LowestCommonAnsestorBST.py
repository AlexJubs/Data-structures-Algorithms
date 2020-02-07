# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: return self.lowestCommonAncestor(root,q,p)
        if p.val < root.val and q.val < root.val: return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val: return self.lowestCommonAncestor(root.right,p,q)
        if p == root or q == root: return root
        if p.val < root.val and q.val > root.val: return root
