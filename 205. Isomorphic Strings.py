class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        
        
        
        visited = set()
        dic = {}
        for i in range(len(s)):
            if (s[i] in dic and t[i] != dic[s[i]]) or (s[i] not in dic and t[i] in visited):
                return False
            else:
                dic[s[i]] = t[i]
                visited.add(t[i])
        
        return True
