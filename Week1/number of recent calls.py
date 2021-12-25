class RecentCounter:

    def __init__(self):
        self.s = []
    def ping(self, t: int) -> int:
        self.s.append(t)
        start = t - 3000
        count = 0
        for i in range(len(self.s)):
            if self.s[0] < start:
                self.s.remove(self.s[0])
            else:
                break
        length = len(self.s)
        return length

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)