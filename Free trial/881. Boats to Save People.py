"""
https://leetcode.com/problems/boats-to-save-people/submissions/
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        count = 0
        left = 0
        right = len(people)-1
        
        while left<=right:
            if people[right] + people[left] > limit:
                count +=1
                right -=1
            else:
                count+=1
                left+=1
                right-=1
        
        return count
        
        
        