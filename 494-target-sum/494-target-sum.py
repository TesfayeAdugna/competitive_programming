class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def findTarget(idx, summ):
            if idx >= len(nums):
                if summ == target:
                    return 1
                return 0
            left = findTarget(idx+1, summ + nums[idx])
            right = findTarget(idx+1, summ - nums[idx])
            
            return left + right
        
        return findTarget(0, 0)
            