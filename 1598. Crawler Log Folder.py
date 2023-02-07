class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i == '../':
                if count>0:
                    count-=1
            elif i != './':
                count+=1
        return count
        
        
