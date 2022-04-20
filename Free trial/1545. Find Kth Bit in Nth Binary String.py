"""
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
"""
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        
        def invert(x):
            x = list(x)
            for i in range(len(x)):
                if x[i] == "0":
                    x[i] = "1"
                else:
                    x[i] = "0"
            return "".join(x)
        
        s = "0"
        for i in range(n):
            x = s[::-1]
            x = invert(x)
            s += "1"
            s += x
            
        return s[k-1]
        