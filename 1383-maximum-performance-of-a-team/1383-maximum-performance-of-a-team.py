class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap, ss, best = [], 0, 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(heap, s)
            ss += s
            ss -= heappop(heap) if len(heap) > k else 0
            best = max(best, ss * e)
        return best % (10**9 + 7)