class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)
        for x in bookings:
            res[x[0]-1] = x[2] + 1
            res[x[1]] = x[2] - 1
        
        if len(res) > n: res.pop(-1)

        for i in range(1,len(res)-1):
            x = res[i] + res[i-1]
            res[i] = x
            
        return res
