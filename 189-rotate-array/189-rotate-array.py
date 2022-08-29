class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        rotatedarray = nums[-k:]
        rotatedarray.extend(nums[:len(nums) - k])
        for i in range(len(nums)):
            nums[i] = rotatedarray[i]
        return nums