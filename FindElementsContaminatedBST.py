# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.nodes = set()
        root.val = 0
        root = self.buildTree(root)
        self.trav(root)

    def buildTree(self, root):
        if root == None: return None
        if root.left != None:
            root.left.val = root.val*2 +1
            root.left = self.buildTree(root.left)
        if root.right != None:
            root.right.val = root.val*2 +2
            root.right = self.buildTree(root.right)
        return root
    
    def trav(self, root):
        if root == None: return
        self.nodes.add(root.val)
        self.trav(root.left)
        self.trav(root.right)
    
    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
