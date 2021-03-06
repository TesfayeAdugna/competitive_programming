"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
class Solution(object):
    def findrange(self,nums,target,flag):
        left = 0
        right = len(nums)-1
        best = -1
        while left<=right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                best = mid
                if flag:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return best
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        result.append(self.findrange(nums,target,True))
        result.append(self.findrange(nums,target,False))
        return result