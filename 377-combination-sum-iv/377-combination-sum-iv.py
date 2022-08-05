class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        
        
        
        
        
        
        
        dp = { 0 : 1 }
        def dfs(target):
            if target in dp:
                return dp[target]
            
            temp = 0
            for num in nums:
                if target > num:
                    temp += dfs(target - num)
                elif target == num:
                    temp += 1
                    
            dp[target] = temp
            
            return temp

        return dfs(target)
        
        
        
#         self.Ans = 0
#         # @lru_cache
#         def dfs(i, total):
#             if total == target:
#                 return 1
            
#             if total>target:
#                 return 0
            
#             for i in range(len(nums)):
#                 self.Ans += dfs(i, total+nums[i])
                    
        
#         dfs(0, 0)
        
#         return self.Ans