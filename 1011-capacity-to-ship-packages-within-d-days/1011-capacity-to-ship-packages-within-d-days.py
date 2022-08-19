class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        
        
        
        
        
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right-left)//2
            
            count = 1
            weightcount = 0
            i = 0
            while i < len(weights):
                if weightcount + weights[i] <= mid:
                    weightcount += weights[i]
                else:
                    weightcount = weights[i]
                    count += 1
                i += 1
                
            if count <= days:
                right = mid
            else:
                left = mid + 1
        return left