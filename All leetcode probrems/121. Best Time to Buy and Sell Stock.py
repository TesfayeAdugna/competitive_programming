"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        
        lst = []
        minimum = prices[0]
        
        for  price in prices:
            if price<minimum:
                minimum = price
            else:
                lst.append(price-minimum)
                
                
                
        return max(lst)