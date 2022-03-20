"""
https://leetcode.com/problems/daily-temperatures/
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0]*len(temperatures)
        
        #keeping future warmer temp in dictionary
        for i in range(len(temperatures)):
            if len(stack)>0 and temperatures[i] > stack[-1][-1]:
                for j in range(len(stack)):
                    if temperatures[i] > stack[-1][1]:
                        temp = stack.pop()
                        output[temp[0]] = i-temp[0]
                    else:
                        break
                stack.append((i,temperatures[i]))
            else:
                stack.append((i,temperatures[i]))
            
        return output
                
                        
        