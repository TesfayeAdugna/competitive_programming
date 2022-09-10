class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
#         n = len(prices)
#         def dfs(idx, flag, summ, trans):
#             if trans > 2*k:
#                 return 0
            
#             self.sidemax = max(summ, self.sidemax)
            
#             for i in range(idx+1, n):
#                 dfs(i, -1 * flag, summ + (flag*prices[i]), trans+1)
                
#             return self.sidemax
        
        
#         Answer = 0
#         for j in range(1, n):
#             self.sidemax = 0
#             side = dfs(j-1, 1, -1 * prices[j-1], 1)
            
#             Answer = max(Answer, side)
            
#         return Answer
    
    
    
    
        @cache
        def dp(i, trans, holding = False):
            if i == len(prices) or trans == k:
                return 0

            buy = dp(i + 1, trans, True) - prices[i] if not holding else 0

            sell = dp(i + 1, trans + 1, False) + prices[i] if holding else 0

            no_action = dp(i + 1, trans, holding)

            return max(buy, sell, no_action)

        return dp(0, 0)    
    
    
    