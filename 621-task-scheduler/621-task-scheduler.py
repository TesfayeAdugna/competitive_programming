class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        heap = []
        for i in count:
            heapq.heappush(heap,-count[i])
            
        time = 0
        queue = deque()
        while heap or queue:
            time+=1
            if heap:
                temp = heapq.heappop(heap)
                if temp+1<0:
                    queue.append([temp+1,time+n])

            if queue and queue[0][1] == time:
                heapq.heappush(heap,queue[0][0])
                queue.popleft()
        
        return time