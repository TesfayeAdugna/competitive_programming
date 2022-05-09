# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Example 2:

# Input: n = 0
# Output: false
# Example 3:

# Input: n = 9
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        count = 0
        def checkpower(n,count):
            if 3**count == n:
                return True
            else:
                if count>=20:
                    return False
                else:
                    count += 1
                    return checkpower(n,count)
                
        return checkpower(n,count)
                