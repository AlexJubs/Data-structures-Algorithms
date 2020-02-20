class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.bills = bills
        self.dp = dict()
        return self.helper(0, 0, 0)
    
    def helper(self, p1, num_5, num_10):
        if self.dp.get((p1,num_5,num_10)) != None: return self.dp[(p1,num_5,num_10)]
        if num_5 < 0 or num_10 < 0:
            self.dp[(p1,num_5,num_10)] = False
            return False
        if p1 >= len(self.bills):
            self.dp[(p1,num_5,num_10)] = True
            return True
        if self.bills[p1] == 5:
            self.dp[(p1,num_5,num_10)] = self.helper(p1+1,num_5+1, num_10)
            return self.helper(p1+1,num_5+1, num_10)
        if self.bills[p1] == 10:
            self.dp[(p1,num_5,num_10)] = self.helper(p1+1, num_5-1, num_10+1)
            return self.helper(p1+1, num_5-1, num_10+1)
        if self.bills[p1] == 20:
            if self.helper(p1+1, num_5-3, num_10) == True:
                self.dp[(p1,num_5,num_10)] = True
                return True
            if self.helper(p1+1, num_5-1, num_10-1) == True:
                self.dp[(p1,num_5,num_10)] = True
                return True
            self.dp[(p1,num_5,num_10)] = False
            return False
