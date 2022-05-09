"""
https://leetcode.com/problems/longest-common-prefix/
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst = []
        i = 0
        while i<200:
            if i <= len(strs[0])-1:
                lst.append(strs[0][i])
            else:
                return "".join(lst)
            for ele in strs:
                if i >= len(ele) or ele[i] != lst[-1]:
                    return "".join(lst[:-1])
            i+=1
        