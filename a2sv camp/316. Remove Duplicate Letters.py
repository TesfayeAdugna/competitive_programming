"""
https://leetcode.com/problems/remove-duplicate-letters/
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
                    
        stack = []
        c = Counter(s)
        for i in s:
            if i not in stack:
                while stack and stack[-1]>i and c[stack[-1]] > 0:
                    stack.pop()
                    
                stack.append(i)
            c[i] -= 1
                    
        return "".join(stack)
        
         