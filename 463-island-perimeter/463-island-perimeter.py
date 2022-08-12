class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        n = len(grid)
        m = len(grid[0])
        visited = set()        
        def dfs(i, j):
            if i>=n or j>=m or i<0 or j<0 or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i,j))
            neighbor = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
            per = 0
            for neigh in neighbor:
                per += dfs(neigh[0], neigh[1])

            return per
            
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    print((x,y))
                    return dfs(x, y)
        return 0