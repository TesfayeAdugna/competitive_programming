"""
https://leetcode.com/problems/fibonacci-number/
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        
        
        memo = {}
        def fibo(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n<=2:
                result = 1
            else:
                result = fibo(n-1) + fibo(n-2)
                
            memo[n] = result
            return result
        
        return fibo(n)
    
    
    
    
    
    