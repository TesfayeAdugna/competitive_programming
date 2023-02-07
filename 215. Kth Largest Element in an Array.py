class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
            
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
            
        return -1*heapq.heappop(nums)
