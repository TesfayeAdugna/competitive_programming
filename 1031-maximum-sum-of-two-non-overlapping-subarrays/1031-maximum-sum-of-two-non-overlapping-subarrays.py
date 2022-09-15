class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        def findMaxSum(prefix, firstlen, secondlen):
            g_max = prefix[firstlen+secondlen-1]
            max1 = prefix[firstlen-1]
            for i in range(len(prefix)-firstlen-secondlen):
                sum1 = prefix[i+firstlen]-prefix[i]
                sum2 = prefix[i+firstlen+secondlen] -prefix[i+firstlen]
                max1 = max(max1, sum1)
                g_max = max(g_max, max1+sum2)
            return g_max
        
        prefixSum = []
        for i in range(len(nums)):
            if not prefixSum:
                prefixSum.append(nums[i])
            else:
                prefixSum.append(prefixSum[-1] + nums[i])
        
        return max(findMaxSum(prefixSum, firstLen, secondLen), findMaxSum(prefixSum, secondLen, firstLen))
        