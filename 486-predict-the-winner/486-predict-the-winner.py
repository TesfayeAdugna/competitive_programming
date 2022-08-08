class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        
        def predict(i, j):
            if i == j:
                return nums[i]
            
            player1 = nums[i] - predict(i+1, j)
            player2 = nums[j] - predict(i, j-1)
            
            return max(player1, player2)
        
        return True if predict(0, len(nums)-1) >= 0 else False
                
        
        
        
        
        
        
        
        
        
        
        
        
                
#         if len(nums) % 2 == 0: n = 0
#         else: n = 1
            
#         self.maxScore = 0
        
#         def predict(nums, left, right):
            
#             if not nums:
#                 self.maxScore = max(self.maxScore, left, right)
#                 return
            
            
#             if len(nums)%2 == n:
#                 left += nums[0]
#                 predict(nums[1:], left, right)
#                 right += nums[-1]
#                 predict(nums[:-1], left, right)
#             else:
#                 if nums[0] >= nums[-1]:
#                     predict(nums[1:], left, right)
#                 else:
#                     predict(nums[:-1], left, right)
                
#             return self.maxScore
    
#         x = predict(nums, 0, 0)
    
#         if x >= sum(nums) - x:
#             return True
#         return False
    
    