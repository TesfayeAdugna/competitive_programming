"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers)-1
        lst = []
        while left<right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                lst.append(left+1)
                lst.append(right+1)
                break
                
        return lst
    
    
    
    
    