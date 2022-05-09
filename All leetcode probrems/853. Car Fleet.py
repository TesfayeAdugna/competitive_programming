"""
https://leetcode.com/problems/car-fleet/
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = []
        for i in range(len(position)):
            temp = [0]*2
            timer = (target-position[i])/speed[i]
            temp[0] = position[i]
            temp[1] = timer
            time.append(temp)
            
        time.sort()
        sortedTime = []
        
        for times in time:
            sortedTime.append(times[1])
        sortedTime=sortedTime[::-1]
        for i in range(len(sortedTime)):
            for j in range(i+1,len(sortedTime)):
                if sortedTime[j] <= sortedTime[i]:
                    sortedTime[j] = sortedTime[i]
                    break
            
        return len(Counter(sortedTime))
            
        