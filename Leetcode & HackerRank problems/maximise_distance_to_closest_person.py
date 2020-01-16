class Solution:
    def closestDist(self, i):
        if i == 0: return self.seats.index(1)
        if i+1 == len(self.seats): return self.seats[::-1].index(1)
        left_dist = 0
        right_dist = 0
        left_offset = 0
        right_offset = 0
        while self.seats[i+right_offset] != 1:
            right_offset = right_offset +1            
            if i+right_offset >= len(self.seats): break
        if right_offset == 1: return 1
        
        while self.seats[i - left_offset] != 1:
            left_offset = left_offset + 1
            if i-left_offset < 0: break
            if left_offset >= right_offset: return left_offset
            
        return min(left_offset, right_offset)
        
    def maxDistToClosest(self, seats: List[int]) -> int:
        if len(seats) == 0: return 0
        res = -1
        self.seats = seats
        for i in range(len(seats)):
            if seats[i] == 0:
                res = max(res,self.closestDist(i))
        
        return res
