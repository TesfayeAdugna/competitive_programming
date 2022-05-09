"""
https://leetcode.com/problems/compare-version-numbers/
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splitted1 = version1.split('.')
        splitted2 = version2.split('.')
        for i in range(len(splitted1)):
            splitted1[i] = int(splitted1[i])
        for i in range(len(splitted2)):
            splitted2[i] = int(splitted2[i])
        
        length = min(len(splitted1), len(splitted2))
        
        for i in range(length):
            if splitted1[i] < splitted2[i]:
                return -1
            if splitted1[i] > splitted2[i]:
                return 1
            
        if sum(splitted1) < sum(splitted2):
            return -1
        if sum(splitted1) > sum(splitted2):
            return 1
        return 0
        