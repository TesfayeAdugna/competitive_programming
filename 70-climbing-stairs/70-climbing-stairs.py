class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        
        cache = {}
        def dp(start):
            if start in cache:
                return cache[start]
            if start == n:
                return 1
            if start > n:
                return 0
            
            climbOne = dp(start + 1)
            climbTwo = dp(start + 2)
            cache[start] = climbOne + climbTwo
            
            return cache[start]
        return dp(0)