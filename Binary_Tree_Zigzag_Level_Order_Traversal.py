# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = list()
        queue = list()
        if root != None: queue.append(root)
        while len(queue) != 0:
            size = len(queue)
            temp = list()
            for i in range(size):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left != None: queue.append(node.left)
                if node.right != None: queue.append(node.right)
            res.append(temp)
        for i in range(1,len(res),2):
            res[i] = res[i][::-1]
        return res
