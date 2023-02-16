class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        maximum_sum = nums[0]
        current_sum = 0
        
        for element in nums:
            if current_sum < 0:
                current_sum = 0
                
            current_sum += element
            maximum_sum = max(current_sum, maximum_sum)
        
        return maximum_sum
