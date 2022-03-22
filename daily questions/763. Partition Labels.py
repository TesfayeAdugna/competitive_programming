"""
https://leetcode.com/problems/partition-labels/
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
                
        count = Counter(s)
        
        temp = 0
        dic = {}
        output = []
        
        for ele in s:
            temp +=1
            count[ele]-=1
            if count[ele] < 1 and ele in dic:
                dic.pop(ele)
            elif ele not in dic and count[ele]>0:
                dic[ele] = 1
                
            if len(dic)<1:
                output.append(temp)
                temp = 0
                
        return output
                        