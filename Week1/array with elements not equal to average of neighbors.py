class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        :https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
        """        
        for i in range(15):
            for j in range(1,len(nums)-1):
                if (nums[j-1] + nums[j+1]) / 2 ==nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
        