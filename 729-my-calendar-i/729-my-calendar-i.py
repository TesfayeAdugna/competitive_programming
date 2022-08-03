class MyCalendar:

    def __init__(self):
        self.stack = []
        
    def book(self, start: int, end: int) -> bool:
        if not self.stack:
            self.stack.append([start, end])
            return True
        else:
            for i in range(len(self.stack)):
                if (start > self.stack[i][0] and start <self.stack[i][1]) or (end>self.stack[i][0] and end<self.stack[i][1]) or (start<=self.stack[i][0] and end>=self.stack[i][1]):
                    return False
            self.stack.append([start, end])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)