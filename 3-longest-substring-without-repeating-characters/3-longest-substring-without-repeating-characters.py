class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        longest = 0
        long_set = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in long_set:
                long_set.add(s[right])
                right += 1
            else:
                long_set.remove(s[left])
                left += 1
            longest = max(longest, right - left)
        return longest