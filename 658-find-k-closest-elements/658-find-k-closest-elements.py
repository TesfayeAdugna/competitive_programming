class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = []
        for i in range(len(arr)):
            temp = abs(arr[i]-x)
            lst.append([temp, arr[i]])
        heapq.heapify(lst)
        answer = []
        while len(answer) < k:
            answer.append(heapq.heappop(lst)[1])
        answer.sort()
        return answer