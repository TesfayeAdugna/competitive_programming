"""
https://leetcode.com/problems/minimum-time-difference/
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        lst = []
        for ele in timePoints:
            lst.append((int(ele[:2])*60) + int(ele[3:]))
            
        lst.sort()
        r = lst[1]-lst[0]
        for i in range(1,len(lst)):
            r = min(r,lst[i]-lst[i-1])
            
        return min(r,1440-(lst[-1]-lst[0]))