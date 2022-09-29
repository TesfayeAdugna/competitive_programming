class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        heap = []
        for i in range(len(nums)):
            temp = abs(nums[i] - 0)
            heap.append([temp, nums[i]])
        heapq.heapify(heap)
        answer = heapq.heappop(heap)
        while heap and heap[0][0] == answer[0]:
            temp = heapq.heappop(heap)
            if temp[1] > answer[1]:
                answer = temp
        return answer[1]