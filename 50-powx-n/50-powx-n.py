class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        dp = {}
        def fn(n):
            if n == 1:
                return x
            if n not in dp:
                dp[n] = fn(n//2) * fn(n-n//2)
            return dp[n]
        
        res = fn(abs(n))
        return res if n>=0 else 1/res