class MyQueue:

    def __init__(self):
        self.s = []
    def push(self, x: int) -> None:
        self.s.append(x)
        return self.s
    def pop(self) -> int:
        a = self.s[0]
        self.s.remove(self.s[0])
        return a
    def peek(self) -> int:
        return self.s[0]
    def empty(self) -> bool:
        if len(self.s)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode 232. Implement Queue using stacks