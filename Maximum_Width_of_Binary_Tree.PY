"""
build a hashmap which maps levels to array of widths. traverse this map and return the max difference in the value array for all levels
"""
from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.levels = defaultdict(list)
        self.trav(root,0,0)
        res = 1
        for y in self.levels.values():
            res = max(res, abs(max(y)-min(y))+1)
        return res
        
    def trav(self, root, depth, pos):
        if root == None: return
        self.levels[depth].append(pos)
        self.trav(root.left, depth+1, 2*pos)
        self.trav(root.right, depth+1, 2*pos +1)
