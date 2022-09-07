class Solution:
    def __init__(self):
        self.dp = {}
        
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n in self.dp:
            return self.dp[n]
        tempAnswer = self.fib(n-1) + self.fib(n-2)
        self.dp[n] = tempAnswer
        return self.dp[n]