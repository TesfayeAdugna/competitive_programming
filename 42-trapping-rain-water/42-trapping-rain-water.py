class Solution:
    def trap(self, height: List[int]) -> int: 
        left = []
        right = []
        for i in range(len(height)):
            if i == 0:
                left.append(i)
                right.append(i)
                continue
                
            if height[i-1] > left[-1]:
                left.append(height[i-1])
            else:
                left.append(left[-1])
                
            if height[-i] > right[-1]:
                right.append(height[-i])
            else:
                right.append(right[-1])
                
        right = right[::-1]
        
        maxArea = 0
        for i in range(len(height)):
            temp = min(left[i], right[i]) - height[i]
            if temp>0:
                maxArea += temp
            
        return maxArea
        
        
        
        
        
        
        
        
        
        
        
        