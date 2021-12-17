class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """        
        m=len(nums)
        for i in range(3):
            for j in range(len(nums)):
                if nums[j] == i:
                    nums.append(i)
        for k in range(m):
            nums.pop(0)
        print(nums)