class Solution:
    def trav(self, path, cur_node):
        if cur_node > len(self.graph): return
        if cur_node == len(self.graph)-1: self.res.append(path + [cur_node])
        for nodes in self.graph[cur_node]:
            self.trav(path + [cur_node], nodes)
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = list()
        self.graph = graph
        self.trav([], 0)
        return self.res