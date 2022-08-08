class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def predict(i, j):
            if i == j:
                return nums[i]
            if (i, j) in dp:
                return dp[(i,j)]
            player1 = nums[i] - predict(i+1, j)
            player2 = nums[j] - predict(i, j-1)
            
            dp[(i,j)] = max(player1, player2)
            
            return dp[(i,j)]
        
        return True if predict(0, len(nums)-1) >= 0 else False
        