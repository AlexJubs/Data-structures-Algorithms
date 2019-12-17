# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generatePaths(self, root, path):
        if root == None: return
        if root.left == None and root.right == None: self.paths.append(path+str(root.val))
        self.generatePaths(root.left, path + str(root.val))
        self.generatePaths(root.right, path + str(root.val))
    
    def binToint(self, b):
        return int(b, 2)
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.paths = list()
        self.generatePaths(root, '')
        return sum(list(map(self.binToint ,self.paths)))
