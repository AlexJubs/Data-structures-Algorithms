class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if len(self.intervals) == 0:
            self.intervals.append([start,end])
            return True
        if self.intersectsInterval(start,end): return False
        else:
            self.intervals.append([start,end])
            return True
    
    def intersectsInterval(self, start,end):
        for x in self.intervals:
            if (start < x[0] and end > x[1]) or (start < x[1] and start >= x[0]) or (end <= x[1] and end > x[0]):
                return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)