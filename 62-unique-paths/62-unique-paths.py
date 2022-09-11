class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(idx1, idx2):
            if idx1 == m-1 and idx2 == n-1:
                return 1
            if idx1 >= m or idx2 >= n:
                return 0
            
            if (idx1, idx2+1) in dp:
                right = dp[(idx1, idx2+1)]
            else:
                right = dfs(idx1, idx2+1)
                
            if (idx1+1, idx2) in dp:
                down = dp[(idx1+1, idx2)]
            else:
                down = dfs(idx1+1, idx2)

            dp[(idx1, idx2)] = right+down
            
            return dp[(idx1, idx2)]
        
        return dfs(0, 0)