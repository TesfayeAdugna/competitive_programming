"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:

1 <= n <= 1690
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        count = 0
        lst = [2,3,5]
        heap = []
        myset = set()
        heapq.heappush(heap,1)
        myset.add(1)
        for i in range(n-1):
            temp = heapq.heappop(heap)
            
            byTwo = temp*2
            if byTwo not in myset: 
                heapq.heappush(heap,byTwo)
                myset.add(byTwo)
            byThree = temp*3
            if byThree not in myset:
                heapq.heappush(heap,byThree)
                myset.add(byThree)
            byFive = temp*5
            if byFive not in myset:
                heapq.heappush(heap,byFive)
                myset.add(byFive)
            
        return heapq.heappop(heap)
                    