"""
https://leetcode.com/problems/string-compression/
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        lst = []
        for i in range(len(chars)):
            if len(lst)<1:
                lst.append([chars[i],1])
            elif lst[-1][0] == chars[i]:
                lst[-1][1]+=1
            else:
                lst.append([chars[i],1])
                        
        new = ""
        for ele in lst:
            if ele[1]>1:
                new+=ele[0]
                new+=str(ele[1])
            else:
                new+=ele[0]
        
        
        for i in range(len(new)):
            chars[i] = new[i]
        return len(new)
        