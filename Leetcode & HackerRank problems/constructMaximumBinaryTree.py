# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])
        root_index = nums.index(max(nums))
        root = TreeNode(nums[root_index])
        root.left = self.constructMaximumBinaryTree(nums[:root_index])
        root.right = self.constructMaximumBinaryTree(nums[root_index+1:])
        return root
