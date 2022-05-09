"""
https://leetcode.com/problems/triangle/
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        for i in range(len(triangle)):
            for j in range(len(triangle[-i-1])-1):
                x = triangle[-i-1][j] + triangle[-i-2][j]
                y = triangle[-i-1][j+1] + triangle[-i-2][j]
                triangle[-i-2][j] = min(x,y)
                

        return triangle[0][0]