class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path1 = list()
        path2 = list()
        while (p != None):
            path1.append(p)
            p = p.parent
        while (q != None):
            path2.append(q)
            q = q.parent
            
        p1 = len(path1)-1
        p2 = len(path2)-1
        while (True):
            if path1[p1] != path2[p2] or p1 < 0 or p2 < 0:
                break
            p1 -= 1
            p2 -= 1
        if path1 == [] or path2 == []: return None
        return path1[p1+1]
