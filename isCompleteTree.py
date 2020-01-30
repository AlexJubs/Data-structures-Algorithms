# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root):
        if root == None: return True
        if root.left == None and root.right == None:
            return self.nodeMap[root.val] == self.maxDepth
        if root.left == None and root.right != None: return False
        return self.helper(root.right) and self.helper(root.left)
    
    def isCompleteTree(self, root: TreeNode) -> bool:
        self.nodeMap = dict()
        self.maxDepth = self.depth(root, 1)
        return self.helper(root)
    
    def depth(self, root, h):
        if root == None: return 0
        self.nodeMap[root.val] = h
        return max(self.depth(root.left,h+1) +1,self.depth(root.right,h+1) +1)
        