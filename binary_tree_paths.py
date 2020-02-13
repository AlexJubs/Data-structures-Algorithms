# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def path(self, root, string):
        if root == None: return
        if root.left == None and root.right == None:
            if string == '': self.res.add('{}'.format(root.val))
            else: self.res.add(string[2:] + '->{}'.format(root.val))
        else:
            self.path(root.left, string+'->{}'.format(root.val))
            self.path(root.right, string+'->{}'.format(root.val))
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = set()
        self.path(root, '')
        return list(self.res)
