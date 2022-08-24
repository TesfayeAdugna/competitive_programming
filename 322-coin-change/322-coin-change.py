class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        

        @lru_cache(None)
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            
            total = float("inf")
            for coin in coins:
                total = min(total, dfs(amount-coin))
                
            return total + 1
        
        answer = dfs(amount)
        if answer < float("inf"):
            return answer
        return -1