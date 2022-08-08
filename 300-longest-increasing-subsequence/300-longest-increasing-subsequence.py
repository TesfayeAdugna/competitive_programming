class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        
        
        
        memo = {}
        largest = 0
        for i in range(len(nums)):
            temp_answer = self.helper(i, nums[i], nums, memo, len(nums))
            largest = max(largest, temp_answer)
            
        return largest
    
        
    def helper(self, index, prev, nums, memo, length):
        
        answer = 0
        for i in range(index + 1, length):
            curr = nums[i]
            if curr > prev:
                if i in memo:
                    possible_answer = memo[i]
                else:
                    possible_answer = self.helper(i, curr, nums, memo, length)
                answer = max(answer, possible_answer)
                
        memo[index] = answer + 1
        return answer + 1