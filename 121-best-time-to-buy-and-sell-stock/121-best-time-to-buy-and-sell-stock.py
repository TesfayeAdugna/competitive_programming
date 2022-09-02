class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        
        
        
        
        ans = 0
        cheapest = prices[0]
        for price in prices:
            if price < cheapest:
                cheapest = price
            else:
                ans = max(ans, price - cheapest)
        return ans
        