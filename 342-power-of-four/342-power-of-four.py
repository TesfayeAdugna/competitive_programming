class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        
        
        
        
        def powerOfFour(n):
            if n == 1:
                return True
            if n == 0 or n%4 != 0:
                return False
            
            return powerOfFour(n//4)
            
        return powerOfFour(n)
        