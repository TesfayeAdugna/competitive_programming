class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        prev = count = 0
        remaining = startFuel
        backup = []
		
        stations.append((target, 0))
        for pos, fuel in stations:
            prev, pos = pos, pos-prev
            
            while remaining < pos and backup:
                remaining += ( -1 * ( heapq.heappop( backup ) ) )
                count += 1
			
            if remaining < pos:
                return -1
			
            remaining -= pos
			
            heapq.heappush(backup, -1 * fuel) 
            
        return count
    
    
    
    
    