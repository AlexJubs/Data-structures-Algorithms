class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        for a in moves:
            if a == 'U': y=y+1
            if a == 'D': y=y-1
            if a == 'R': x=x+1
            if a == 'L': x=x-1
        return x == 0 and y == 0