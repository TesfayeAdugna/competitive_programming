class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        
        
        subarrayCount = 0
        left,right = 0,0
        queue = deque()
        
        while right < len(nums):
            if nums[right] % 2 != 0: 
                queue.append(right)
            
            if len(queue) > k:
                while len(queue) > k:
                    if nums[left] % 2 != 0: 
                        queue.popleft()
                    left += 1
            
            if len(queue) == k: 
                subarrayCount += queue[0] - left + 1
            
            right += 1
            
        
        return subarrayCount

        
        
        
#         left = 0
#         right = 0
#         odd = 0
#         ans = 0
#         while right < len(nums):
#             if odd < k:
#                 if nums[right]%2 == 1:
#                     odd += 1
#                 right += 1
#             else:
#                 if nums[left]%2 == 1:
#                     odd -= 1
#                 left += 1
#             if odd == k:
#                 ans += 1
#         return ans