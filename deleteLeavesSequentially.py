# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeaf(self, root):
        if root == None: return False
        return root.left == None and root.right == None
    
    def removeLeaf(self, root, target):
        if root == None: return
        if self.isLeaf(root) and root.val == target: return None
        if self.isLeaf(root.left) and root.left.val == target: root.left = None
        if self.isLeaf(root.right) and root.right.val == target: root.right = None
        root.left = self.removeLeaf(root.left, target)
        root.right = self.removeLeaf(root.right, target)
        return root
    
    def LeafInTree(self, root, target):
        if root == None: return False
        if root.left == None and root.right == None:
            if root.val == target: return True
        return self.LeafInTree(root.left, target) or self.LeafInTree(root.right, target)
        
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        while self.LeafInTree(root, target):
            root = self.removeLeaf(root, target)
        return root
