class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        
        
        
        ans = 0
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
                
            if stack[-1] == "R" and s[i] == "L":
                stack.pop()
            elif stack[-1] == "L" and s[i] == "R":
                stack.pop()
            else:
                stack.append(s[i])
            
            if not stack:
                ans += 1
        return ans
            