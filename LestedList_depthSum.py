
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.res = 0
        self.dfs(nestedList, 1)
        return self.res
    
    def dfs(self, nestedList, depth):
        for x in nestedList:
            if x.getInteger() != None: self.res = self.res + x.getInteger()*depth
            if x.getList() != None: self.dfs(x.getList(), depth+1)
    
    
    
    
