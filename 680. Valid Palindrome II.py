class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        
        
        
        
        
        
        i = 0
        j = len(s)-1
        count = 1
        ans = True
        while i<len(s)//2:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i] == s[j-1] and count>0:
                    j -= 1
                    count -= 1
                else:
                    ans = False
                    break
        i = 0
        j = len(s)-1
        count = 1
        ans2 = True
        while i<len(s)//2:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i+1] == s[j] and count>0:
                    i += 1
                    count -= 1
                else:
                    ans2 = False
                    break
                
                
        return ans or ans2
    
    
