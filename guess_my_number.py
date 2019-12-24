class Solution:
    def guessNumber(self, n: int) -> int:
        return self.helper(n//2, n//2)
    
    def helper(self, n, window):
        res = guess(n)
        if res == 0: return n
        if res == 1: 
            if n != n + window: return self.helper(n + window, window//2)
            else: return self.helper(n+1, window)
        if res == -1:
            if n != n - window: return self.helper(n - window, window//2)
            else: return self.helper(n-1, window)
