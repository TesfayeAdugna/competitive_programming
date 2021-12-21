class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maximumpair = []
        length = len(nums)//2
        for i in range(length):
            maximumpair.append(nums[i]+nums[-i-1])
                        
        return max(maximumpair)
             