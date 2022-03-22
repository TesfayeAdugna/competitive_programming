"""
https://leetcode.com/problems/partition-labels/
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
                
        count = Counter(s)
        
        lst = []
        dic = {}
        output = []
        
        for ele in s:
            lst.append(ele)
            count[ele]-=1
            if count[ele] < 1 and ele in dic:
                dic.pop(ele)
            elif ele not in dic and count[ele]>0:
                dic[ele] = 1
                
            if len(dic)<1:
                output.append(len(lst))
                lst = []
                
        return output
                        