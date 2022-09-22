class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        
        
        
        
        
        s_lst = s.split()
        for i in range(len(s_lst)):
            s_lst[i] = s_lst[i][::-1]
        return " ".join(s_lst)
        