class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        memo = {}
        def dp(idx):
            if idx in memo:
                return memo[idx]
            if idx >= len(cost):
                return 0
            if idx == len(cost) or idx == len(cost)-1:
                return cost[idx]
            
            left = cost[idx] + dp(idx+1)
            right = cost[idx] + dp(idx+2)
            memo[idx] = min(left, right)
            return memo[idx]
    
        return min(dp(0), dp(1))