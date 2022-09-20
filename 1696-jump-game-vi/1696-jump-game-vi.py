class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)-1
        heap = []
        ans = nums[n]
        heapq.heappush(heap, (-nums[-1], n))
        
        for i in range(n-1, -1, -1):
            while i+k < heap[0][1]:
                heapq.heappop(heap)
                
            ans = nums[i] + (heap[0][0] * -1)
            heapq.heappush(heap, (-ans, i))

        return ans
        
        
        
#         @lru_cache(None)
#         def dfs(idx):
#             # base case
#             if idx == len(nums)-1:
#                 return nums[idx]
#             # recursive calls
#             maxSum = -1000000000
#             for i in range(idx+1, min(idx+k, len(nums))+1):
#                 res = nums[idx] + dfs(i)
#                 maxSum = max(maxSum, res)
                
#             return maxSum
        
#         return dfs(0)