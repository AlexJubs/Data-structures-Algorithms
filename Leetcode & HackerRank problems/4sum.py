class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        comp = dict()
        for numA in A:
            for numB in B:
                if comp.get(numA+numB) == None: comp[numA+numB] = 0
                comp[numA+numB] = comp[numA+numB] + 1
        for x in C:
            for y in D:
                if comp.get(-1*(x+y)) != None: 
                    res = res + comp[-1*(x+y)]
        return res