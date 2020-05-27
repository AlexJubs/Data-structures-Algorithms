class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        self.piles = sorted(piles)
        self.H = H
        # we can do a simple binary search to find the correct speed, starting at a very large number
        return self.binary_search(left=0, right=999999999)
    
    def can_eat_bananas(self, speed):
        time = 0
        if speed >= self.piles[-1] and self.H >= len(self.piles): return True
        if speed == 0: return False
        
        for x in self.piles:
            time = time + int(x/speed) + 1
            if (int(x/speed) == x/speed): time = time -1
            if time > self.H: return False
        return time <= self.H
    
    def binary_search(self, left, right):
        if (right >= left):
            mid = left + (right-left)//2
            
            if self.can_eat_bananas(mid) and (self.can_eat_bananas(mid-1) == False):
                return mid
            if self.can_eat_bananas(mid) == False: # too small
                return self.binary_search(mid,right)
            
            if self.can_eat_bananas(mid): # too large
                return self.binary_search(left, mid)
                
