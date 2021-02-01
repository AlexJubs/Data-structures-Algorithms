# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None: return []
        self.res = [root.val]
        self.trav(root, 0)
        return self.res
    
    def trav(self, root, depth):
        if root == None: return
        if depth >= len(self.res): self.res.append(root.val)
        self.trav(root.right, depth+1)
        self.trav(root.left, depth+1)
        
