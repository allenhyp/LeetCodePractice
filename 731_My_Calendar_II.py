class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if start < e and end > s:
                return False
        for s, e in self.calender:
            if start < e and end > s:
                self.overlap.append((max(start, s), min(end, e)))
        self.calender.append((start, end))
        return True
                


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
