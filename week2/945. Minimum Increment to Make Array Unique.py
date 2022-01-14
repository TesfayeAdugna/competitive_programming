class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        count = 0
        temp = nums[0]
        for i in nums:
            if i>temp:
                temp = i+1
            else:
                count += temp -i
                temp += 1
        return count