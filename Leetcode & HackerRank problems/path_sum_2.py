class Solution:
    def path(self, root, arr, path_s):
        if root == None: return
        if root.left == None and root.right == None:
            if path_s + root.val == self.target_sum: self.res.append(arr + [root.val])
            return
        
        self.path(root.left, arr + [root.val], path_s + root.val)
        self.path(root.right, arr + [root.val], path_s + root.val)
            
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.res = list()
        self.target_sum = s
        self.path(root, [], 0)
        return self.res