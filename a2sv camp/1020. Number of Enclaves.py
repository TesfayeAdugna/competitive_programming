"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""

class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(index1,index2):
            if index1<0 or index2<0 or index1 == m or index2 == n or grid[index1][index2] == 0:
                return
            
            grid[index1][index2] = 0
            dfs(index1,index2+1)
            dfs(index1,index2-1)
            dfs(index1+1,index2)
            dfs(index1-1,index2)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1:
                    if grid[i][j] == 1:
                        dfs(i,j)
                        
                if j == 0 or j == n-1:
                    if grid[i][j] == 1:
                        dfs(i,j)
                        
        answer = 0
        for k in range(m):
            for j in range(n):
                if grid[k][j] == 1:
                    answer+=1
                    
        return answer