"""
https://leetcode.com/contest/weekly-contest-120/problems/squares-of-a-sorted-array/
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
            
            
        nums.sort()
        
        return nums
        