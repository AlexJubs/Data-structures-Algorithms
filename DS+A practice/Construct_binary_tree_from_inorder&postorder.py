"""
InOrder = L,root,R  PostOrder = L,R,root. The root of the tree will be PostOrder[-1]. The inorder and postorder arrays must be the same length. if len == 0: return none, if len == 1: return node(post[-1])
The left child's inorder = inorder[0 -> index(root)],
The left child's postorder = postorder[0 -> inorder's index of root]
The right child's inorder = inorder[index(root) -> len]
The right child's postorder = postorder[inorder's index of root +1 -> len-1]
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if (len(inorder) == 0 or len(postorder) == 0): return None
        if (len(inorder) == 1 and len(postorder) == 1): return TreeNode(postorder[-1])
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:len(postorder)-1])
        return root