"""
https://leetcode.com/problems/max-consecutive-ones-iii/
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxx = 0
        queue = deque()
        for i in range(len(nums)):
            if nums[i] == 0 and k>0:
                queue.append(nums[i])
                k -= 1
            elif nums[i] == 1:
                queue.append(nums[i])
            elif nums[i] == 0 and k == 0:
                while len(queue) > 0 and queue[0] != 0:
                    queue.popleft()
                if queue:
                    queue.popleft()
                    queue.append(nums[i])
            maxx = max(maxx,len(queue))
            
        return maxx
        