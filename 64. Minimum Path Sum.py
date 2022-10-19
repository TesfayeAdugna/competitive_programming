class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:


        m = len(grid)
        n = len(grid[0])
        @lru_cache(None)
        def dfs(row, col):
            if row >= m or col >= n:
                return 1000
            if row == m-1 and col == n-1:
                return grid[row][col]
            
            right = grid[row][col] + dfs(row, col+1)
            down = grid[row][col] + dfs(row+1, col)

            return min(right, down)
        
        return dfs(0, 0)
