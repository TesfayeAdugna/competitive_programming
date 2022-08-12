class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = abs(n)
        dp = {}
        def fn(n):
            if n == 1:
                return x
            if n not in dp:
                dp[n] = fn(n//2) * fn(n-n//2)
            return dp[n]
        
        return fn(n)