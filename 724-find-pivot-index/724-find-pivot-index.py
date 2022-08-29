class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left, pivot, right = 0, 0, sum(nums)-nums[0]
        while pivot < len(nums)-1 and right != left:
            print("left: ", left, "right: ", right)
            pivot += 1
            right -= nums[pivot]
            left += nums[pivot-1]
            
        return pivot if left == right else -1
    
    """
    1, 7, 3, 6, 5, 6
    
    1, 8, 11, 17, 22, 28
    
    left = 0
    pivot = 0
    
    """