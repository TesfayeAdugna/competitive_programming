class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        
                
        longest = 0
        answer = ""
        for i in range(len(s)):
            # odd case
            left, right = i-1, i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left + 1 > longest:
                longest = right-left + 1
                answer = s[left+1: right]
                
            # even case
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    left, right = i-1, i+2
                    while left>=0 and right<len(s) and s[left] == s[right]:
                        left -= 1
                        right += 1
                    if right - left + 1 > longest:
                        longest = right-left+1
                        answer = s[left+1:right]
                
        return answer
        
        
#         self.longest = 0
#         @lru_cache(1000)
#         def dfs(start, end):
#             if start >= end:
#                 return (start, end)
#             if end - start > self.longest:
#                 if isPalindrom(start, end-1):
#                     return (start, end)
            
#             left = dfs(start+1, end)
#             right = dfs(start, end-1)
            
#             answer = left if left[1] - left[0] > right[1] - right[0] else right
#             self.longest = max(self.longest, answer[1]-answer[0])
#             return answer

#         res = dfs(0, len(s))
        
#         return s[res[0]:res[1]]
        
        
        
        