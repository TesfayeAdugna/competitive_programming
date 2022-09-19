class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        
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