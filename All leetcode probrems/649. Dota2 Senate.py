"""
https://leetcode.com/problems/dota2-senate/
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        
        Dqueue = deque()
        Rqueue = deque()
        
        length = len(senate)
        
        for i in range(length):
            if senate[i] == 'D':
                Dqueue.append(i)
            else:
                Rqueue.append(i)
                
        while Dqueue and Rqueue:
            rindex = Rqueue.popleft()
            dindex = Dqueue.popleft()
            
            if rindex<dindex:
                Rqueue.append(rindex+length)
            else:
                Dqueue.append(dindex+length)
                
        if Dqueue:
            return "Dire"
        else:
            return "Radiant"
        
        
        
        
        
        