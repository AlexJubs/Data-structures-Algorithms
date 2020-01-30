# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
 inOrder: L root R, preOrder: root L R. the root will be preorder[0]. the left child's inorder will be inorder[:root] the preorder will be preorder[1:end of left] (1 because we dont indluce the root). the right child's inorder will be inorder[root:] the preorder will be preorder[end of left:]
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if (len(preorder) == 0 or len(inorder) == 0): return None
        if (len(preorder) == 1 and len(inorder) == 1): return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:inorder.index(preorder[0])+1], inorder[:inorder.index(preorder[0])])
        root.right = self.buildTree(preorder[inorder.index(preorder[0])+1:], inorder[inorder.index(preorder[0])+1:])
        return root