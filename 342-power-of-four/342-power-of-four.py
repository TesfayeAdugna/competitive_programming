class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        
        init = 1
        while init <= n:
            if init ^ n == 0:
                return True
            init *=4
        
        return False
                