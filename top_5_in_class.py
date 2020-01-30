class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        grades = dict()
        count = dict()
        res = list()
        for stud in items:
            if grades.get(stud[0]) == None:
                grades[stud[0]] = tuple([stud[1]])
                count[stud[0]] = 1
            else:
                grades[stud[0]] = grades[stud[0]] + tuple([stud[1]])
                count[stud[0]] = count[stud[0]] + 1
                
                if count[stud[0]] > 5:
                    temp = list(grades[stud[0]])
                    temp.remove(min(temp))
                    grades[stud[0]] = tuple(temp)
                    count[stud[0]] = 5
                    
        for x,y in grades.items():
            res.append([x, int(sum(y)/count[x])])
        return res
                    
                    