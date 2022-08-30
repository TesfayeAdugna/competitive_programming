class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        
        
        g.sort()
        s.sort()
        Answer = 0        
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1
                i += 1
                Answer += 1
            else:
                while j< len(s) and s[j] < g[i]:
                    j += 1
        return Answer