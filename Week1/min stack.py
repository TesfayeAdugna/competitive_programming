class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        return self.s
    def pop(self) -> None:
        temp = self.s[-1]
        self.s.pop()
        return temp

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return min(self.s)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()