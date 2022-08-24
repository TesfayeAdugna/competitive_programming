class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        
        
        def Power(n):
            if n == 1:
                return True
            if n%3 != 0 or n < 1:
                return False
            return Power(n//3)
        
        return Power(n)