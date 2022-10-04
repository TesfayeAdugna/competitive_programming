class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        abcabc
          l
             r
        """
        left, right, ans, dic, l = 0, 0, 0, {}, len(s)
        while right < l or len(dic) == 3:
            if len(dic) < 3:
                if s[right] in dic:
                    dic[s[right]] += 1
                else:
                    dic[s[right]] = 1
                right += 1
            else:
                ans += l - right + 1
                if dic[s[left]] > 1:
                    dic[s[left]] -= 1
                else:
                    del dic[s[left]]
                left += 1
        return ans
