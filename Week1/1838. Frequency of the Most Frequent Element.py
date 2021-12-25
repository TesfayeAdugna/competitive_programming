class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
             
        nums = sorted(nums)
        maxFrequency = 1
        lst = len(nums)-1
        bob = len(nums)-1
        while bob >= maxFrequency:
            while lst and k - (nums[bob] - nums[lst - 1]) >= 0:
                k -= nums[bob] - nums[lst - 1]
                lst -= 1
            maxFrequency = max(maxFrequency, bob - lst + 1)
            k += (bob - lst) * (nums[bob] - nums[bob - 1])
            bob -= 1
        return maxFrequency