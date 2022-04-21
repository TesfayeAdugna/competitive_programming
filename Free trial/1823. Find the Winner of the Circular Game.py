"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        
        lst = [x for x in range(1,n+1)]
        i = 0
        while len(lst)>1:
            temp = k
            while temp > 1:
                if i== len(lst)-1:
                    i = 0
                else:
                    i+=1
                temp -=1
            lst.pop(i)
            if i>len(lst)-1:
                i = 0
        return lst[0]