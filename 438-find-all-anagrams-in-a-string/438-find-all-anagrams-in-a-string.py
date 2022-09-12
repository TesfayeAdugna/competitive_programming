class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        Answer = []
        left = 0
        right = len(p) - 1
        substring = s[left:right+1]
        sub_count = Counter(substring)
        p_count = Counter(p)
        while right < len(s):
            if p_count == sub_count:
                Answer.append(left)
                
            if sub_count[s[left]] > 1:
                sub_count[s[left]] -= 1
            else:
                del sub_count[s[left]]
            
            left += 1
            right += 1
            if right < len(s):
                if s[right] in sub_count:
                    sub_count[s[right]] += 1
                else:
                    sub_count[s[right]] = 1
                
        return Answer