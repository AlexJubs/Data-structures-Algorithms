# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def avg(self, arr):
        if arr != []:
            return sum(arr)/len(arr)
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
            res.append(self.avg(temp))
        return res
