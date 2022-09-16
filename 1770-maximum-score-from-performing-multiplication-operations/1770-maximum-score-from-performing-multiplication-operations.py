class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        
        
        
        n = len(nums)
        m = len(multipliers)
        dp = {}
        @lru_cache(2000)
        def dfs(start, end):
            index = start+n-end-1
            # base case
            if index >= len(multipliers):
                return 0
            
            # if (start, end) in dp:
            #     return dp[(start, end)]
            
            right = multipliers[index] * nums[end] + dfs(start, end-1)
            left = multipliers[index]  * nums[start] + dfs(start+1, end)
                
            # dp[(start, end)] =  max(right, left)
            
            return max(right, left)
        
        return dfs(0, n-1)