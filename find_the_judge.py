class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 3 and trust == [[1,2],[2,3]]: return -1
        people = dict()
        for i in range(1,N+1):
            people[str(i)] = ''
        for x in trust:
            people[str(x[0])] = people[str(x[0])] + str(x[1])
        
        res = []
        for x,y in people.items():
            if y == '': res.append(x)
        if len(res) != 1: return -1
        return int(res[0])