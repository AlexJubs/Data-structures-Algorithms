"""
build a hashMap mapping every node to its depth. trav the right child and append those nodes until you reach the deepest left node. Then append the RIGHTMOST left children which have depth. Each depth will have a rightmost positioned node. append this
"""

class Solution:
    def trav(self, root, depth, pos):
        if root == None: return
        if self.nodes.get(depth) == None or self.nodes[depth][1] <= pos:
            self.nodes[depth] = tuple([root,pos])
        self.trav(root.left, depth+1, pos-1)
        self.trav(root.right, depth+1, pos+1)
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None: return None
        if root.left == None and root.right == None: return [root.val]
        self.nodes = dict() # depth -> (node, pos)
        self.trav(root, 0, 0)
        L = list()
        for x,y in self.nodes.items(): L.append([x,y[0],y[1]])
        L.sort(key=lambda e: e[0])
        res = list(map(lambda e: e[1].val, L)
	
	return res
