# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def travHorizontalDist(self, root, dist, height):
        if root == None: return
        self.horizontal_distances[root.val] = dist
        self.vertical_dist[root.val] = height
        self.rows.add(dist)
        self.travHorizontalDist(root.left, dist-1, height+1)
        self.travHorizontalDist(root.right, dist+1, height+1)
        
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return None
        res = list()
        self.rows = set()
        self.horizontal_distances = dict()
        self.vertical_dist = dict()
        self.travHorizontalDist(root, 0, 0)
        
        for i in range(len(self.rows)): res.append([])
        offset = -1*(min(self.rows))
        
        for x,y in self.horizontal_distances.items():
            res[y+offset].append(x)
            
        for i in range(len(res)):
            res[i] = sorted(res[i], key = lambda p: self.vertical_dist[p])
                
        return res