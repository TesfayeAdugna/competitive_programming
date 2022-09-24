class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        
        
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return nums[i]
            else:
                nums_set.add(nums[i])