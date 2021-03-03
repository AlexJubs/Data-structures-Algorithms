class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexes = dict()
        for i in range(len(list1)):
            indexes[list1[i]] = i
                
        res_ind = []
        m = 9999
        for i in range(len(list2)):
            if indexes.get(list2[i]) != None:
                if m == 9999:
                    res_ind.append(i)
                    m = indexes[list2[i]] + i
                    
                elif indexes[list2[i]] + i == m:
                    res_ind.append(i)
                    
                elif indexes[list2[i]] + i < m:
                    res_ind = [i]
                    m = indexes[list2[i]] + i

        def f(i): return list2[i]
        
        return list(map(f,res_ind))
