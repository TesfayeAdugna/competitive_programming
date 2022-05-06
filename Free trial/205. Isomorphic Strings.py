"""
https://leetcode.com/problems/isomorphic-strings/
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        sett = set()
        for i in range(len(s)):
            if t[i] in sett and s[i] not in dic:
                return False
            if s[i] not in dic:
                dic[s[i]] = t[i]
                sett.add(t[i])
            elif t[i] != dic[s[i]]:
                return False
        return True