class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack_s = []
        stack_t = []
        
        i = 0
        while i < len(s):
            if s[i] != "#":
                stack_s.append(s[i])
            else:
                if stack_s:
                    stack_s.pop()
            i += 1
                    
        j = 0
        while j < len(t):
            if t[j] != "#":
                stack_t.append(t[j])
            else:
                if stack_t:
                    stack_t.pop()
            j += 1
            
        return stack_s == stack_t