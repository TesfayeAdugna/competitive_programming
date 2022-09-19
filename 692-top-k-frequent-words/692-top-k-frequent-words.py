class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        list1 = []
        for i in count:
            list1.append((-1*count[i],i))
                    
        heapq.heapify(list1)
        result = []
        
        n = 0
        while n<k:
            result.append(heapq.heappop(list1)[1])
            n+=1
            
        return result