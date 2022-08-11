class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        
        
        
        
        
        if len(nums) == 1: return nums[0]
        @lru_cache
        def robber(index):
            if index >= len(nums)-2:
                return nums[index]
            
            left = nums[index] + robber(index+2)
            right = nums[index] + robber(index+3) if index < len(nums)-3 else 0
            
            return max(left, right)
        
        return max(robber(0), robber(1))