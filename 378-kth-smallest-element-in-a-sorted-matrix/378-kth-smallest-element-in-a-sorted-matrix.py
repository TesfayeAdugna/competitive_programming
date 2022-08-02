class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = []
        n = len(matrix)
        for i in range(n):
            for val in matrix[i]:
                if len(heap) < k:
                    heapq.heappush(heap, -1*val)
                else:
                    heapq.heappushpop(heap, -1*val)
        return -1*heap[0]