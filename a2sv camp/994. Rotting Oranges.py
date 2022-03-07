"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        self.answer = 0
        
        def bfs(queue):
            
            while queue:
                size = len(queue)
                count = 0
                for i in range(size):
                    i1, i2 = queue.popleft()
                    if i1>0 and grid[i1-1][i2]==1:
                        grid[i1-1][i2] = 2
                        queue.append((i1-1,i2))
                        count+=1
                    if i1<m-1 and grid[i1+1][i2] == 1:
                        grid[i1+1][i2] = 2
                        queue.append((i1+1,i2))
                        count+=1
                    if i2>0 and grid[i1][i2-1] ==1:
                        grid[i1][i2-1]=2
                        queue.append((i1,i2-1))
                        count+=1
                    if i2<n-1 and grid[i1][i2+1] == 1:
                        grid[i1][i2+1] = 2
                        queue.append((i1,i2+1))
                        count+=1
                if count>0:
                    self.answer+=1
                            
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    
        bfs(queue)
                    
        for k in range(m):
            for l in range(n):
                if grid[k][l]==1:
                    return -1
                    
        return self.answer
        
        
        
        