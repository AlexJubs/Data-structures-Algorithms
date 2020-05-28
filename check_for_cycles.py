class Solution:
    def dfs(self, edges, target):
        for vertex in edges:
            if vertex == target: return True
            if (self.dfs(self.connections[vertex], target)): return True
        return False
        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # we have a graph with N edges and we want to check if it is cyclic or not
        self.connections = dict()
        for i in range(1,N+1): self.connections[i] = list()
            
        # building the connections mapping (maps vertex to its connections using the edges list)
        for x in dislikes:
            self.connections[x[0]].append(x[1])
            
        print(self.connections)
        for i in range(1,N+1):
            if self.dfs(self.connections[i], i): return False # if we find a cycle
            
        return True
