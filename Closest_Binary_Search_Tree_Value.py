# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inOrderTrav(self, root):
        if root != None:
            self.inOrderTrav(root.left)
            self.arr.append(root.val)
            self.inOrderTrav(root.right)
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        self.arr = list()
        self.inOrderTrav(root)
        if k >= len(self.arr): return self.arr
        res = list()
        delta = float('inf')
        for i in range(len(self.arr)):
            if abs(target-self.arr[i]) < delta:
                delta = abs(target-self.arr[i])
                middle = i
        if k == 1: return [self.arr[middle]]
        left = middle -1
        right = middle+1
        res.append(self.arr[middle])
        while len(res) != k:
            if left < 0:
                res.append(self.arr[right])
                right = right+1
            elif right >= len(self.arr):
                res.append(self.arr[left])
                left = left-1
            elif abs(self.arr[left]-target) <= abs(self.arr[right]-target):
                res.append(self.arr[left])
                left = left-1
            elif abs(self.arr[right]-target) < abs(self.arr[left]-target):
                res.append(self.arr[right])
                right = right+1
        return res