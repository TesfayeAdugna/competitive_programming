class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        
        
        
        
        
        if len(nums) == 1: return nums[0]
        dic = {}
        def robber(index):
            if index in dic:
                return dic[index]
            if index >= len(nums)-2:
                return nums[index]
            
            left = nums[index] + robber(index+2)
            right = nums[index] + robber(index+3) if index < len(nums)-3 else 0
            dic[index] = max(left, right)
            return dic[index]
        
        return max(robber(0), robber(1))