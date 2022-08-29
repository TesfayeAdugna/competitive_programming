class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        prefixsum = []
        suffixsum = []
        for i in range(len(nums)):
            if not prefixsum:
                prefixsum.append(nums[i])
            else:
                prefixsum.append(prefixsum[-1] + nums[i])
            
            if not suffixsum:
                suffixsum.append(nums[-i-1])
            else:
                suffixsum.append(suffixsum[-1] + nums[-i-1])
                
        suffixsum = suffixsum[::-1]
        
        for i in range(len(nums)):
            if suffixsum[i] == prefixsum[i]:
                return i
        return -1
        
#         left, pivot, right = 0, 0, sum(nums)-nums[0]
#         while pivot < len(nums)-1 and right != left:
#             pivot += 1
#             right -= nums[pivot]
#             left += nums[pivot-1]
            
#         return pivot if left == right else -1
        
    
    
    """
    1, 8, 11, 17, 22, 6
    28, 27, 20, 17, 11, 6
    
    1, 3, 6
    6, 5, 3
    
    2, 3, 2
    2, 0, -1
    
    """