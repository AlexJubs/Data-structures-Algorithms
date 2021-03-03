"""
Find the deepest node depth of the root, then find the deepest node depth of the left and right children, if they are equal then return root. Otherwise recurse on the child which has the greater maxdepth.
"""

class Solution:
    def deepest(self, root):
        if root == None: return 0
        return max(self.deepest(root.left),self.deepest(root.right))+1
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root == None or (root.left == None and root.right == None): return root
        a, b = self.deepest(root.left), self.deepest(root.right)
        if a == b: return root
        elif a > b: return self.subtreeWithAllDeepest(root.left)
        else: return self.subtreeWithAllDeepest(root.right)
