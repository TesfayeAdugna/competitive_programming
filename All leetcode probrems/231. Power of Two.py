"""
https://leetcode.com/problems/power-of-two/
"""
def isPowerOfTwo(self, n: int) -> bool:
    return n&n-1==0 if n>0 else False