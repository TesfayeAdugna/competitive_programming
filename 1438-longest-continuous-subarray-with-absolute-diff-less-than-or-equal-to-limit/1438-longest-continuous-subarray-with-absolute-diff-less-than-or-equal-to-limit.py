class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxLen = 0
        i = 0
        minQueue = deque()
        maxQueue = deque()
        for j in range(len(nums)):
            while minQueue and minQueue[-1] > nums[j]:
                minQueue.pop()
            minQueue.append(nums[j])
            while maxQueue and maxQueue[-1] < nums[j]:
                maxQueue.pop()
            maxQueue.append(nums[j])
            if maxQueue[0] - minQueue[0] <= limit:
                maxLen = max(maxLen, j-i+1)
            else:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                    
                i += 1

        return maxLen 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         answer = 0
#         queue = deque([nums[0]])
#         maxx = minn = nums[0]
        
#         for i in range(1, len(nums)):            
#             temp = nums[i]
#             if temp > maxx: maxx = temp
#             elif temp < minn: minn = temp
                
#             while max(temp, maxx) - min(temp, minn) > limit:
#                 delete = queue.popleft()
#                 if delete == minn:
#                     if queue and temp>minn:
#                         minn = min(queue)
#                     else:
#                         minn = temp
#                 if delete == maxx:
#                     if queue and temp<maxx:
#                         maxx = max(queue)
#                     else:
#                         maxx = temp
                    
            
#             queue.append(temp)
#             answer = max(answer, len(queue))
            
#         return answer if answer>0 else 1
            
            