"""
We're trying to find the minimum costs. We do this by considering every possible combination
"""
class Solution:
    def helper(self, a, b, arr, tot):
        if (a == 0 and b == 0): return tot
        if a == 0: return self.helper(a,b-1,arr[1:],arr[0][1]+tot)
        if b == 0: return self.helper(a-1,b,arr[1:],arr[0][0]+tot)
        A = self.helper(a-1,b,arr[1:],tot+arr[0][0])
        B = self.helper(a,b-1,arr[1:],tot+arr[0][1])
        return min(A,B)
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return self.helper(len(costs)/2,len(costs)/2,costs,0)
    