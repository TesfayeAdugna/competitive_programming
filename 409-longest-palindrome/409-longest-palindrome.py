class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        
        
        
        count_s = Counter(s)
        ans = 0
        maxx_odd = 0
        flag = True
        for key in count_s:
            if count_s[key]%2 == 0:
                ans += count_s[key]
            else:
                if count_s[key] > 1:
                    ans += count_s[key] -1
                    maxx_odd = 1
                else:
                    if flag:
                        ans += count_s[key]
                        flag = False
        if flag:
            ans += maxx_odd
        return ans