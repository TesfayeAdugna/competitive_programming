"""
https://leetcode.com/problems/sum-of-subarray-ranges/
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
    
        summ = 0
        for i in range(len(nums)):
            minn = nums[i]
            maxx = nums[i]
            for j in range(i,len(nums)):                
                if nums[j] < minn:
                    minn = nums[j]
                if nums[j] > maxx:
                    maxx = nums[j]
                    
                summ += maxx - minn
                
        return summ
        