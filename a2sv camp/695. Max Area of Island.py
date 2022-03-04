"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        lst = []
        m = len(grid)
        n = len(grid[0])
        answer = 0
        
        def dfs(index1,index2):
            if index1<0 or index2<0 or index1 == m or index2 == n or grid[index1][index2] == 0:
                return
            grid[index1][index2] = 0
            self.count += 1
                
            dfs(index1,index2+1)
            dfs(index1,index2-1)
            dfs(index1+1,index2)
            dfs(index1-1,index2)
            
            return self.count
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.count = 0
                    answer = max(dfs(i,j),answer)
                    
        return answer
    
    