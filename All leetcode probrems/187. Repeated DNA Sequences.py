"""
https://leetcode.com/problems/repeated-dna-sequences/
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
    
        if len(s)<10:
            return []
        
        dic = {}
        
        for i in range(len(s)):
            if i+9 < len(s):
                last = i+10
            else:
                last = len(s)-1
                
            todo = s[i:last]
            
            if todo in dic:
                dic[todo]+=1
            else:
                dic[todo] = 1
                
        
        lst = []
        for ele in dic:
            if ele != '' and dic[ele]>1:
                lst.append(ele)

        return lst
        
        
                