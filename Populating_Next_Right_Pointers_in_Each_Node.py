"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connectLeftRight(self, root):
        left, right = root.left, root.right
        while left != None or right != None:
            left.next = right
            left = left.right
            right = right.left
        
    def connect(self, root: 'Node') -> 'Node':
        if root == None or root.left == None: return root
        root.left = self.connect(root.left)
        root.right = self.connect(root.right)
        self.connectLeftRight(root)
        return root
