"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return ""
        
        dic = {'2': ['a','b','c'],'3': ['d','e','f'],'4': ['g','h','i'],
            '5': ['j','k','l'],'6': ['m','n','o'],'7': ['p','q','r','s'],
            '8': ['t','u','v'],'9': ['w','x','y','z']}
        lst = []
        for i in digits:
            lst.append(dic[i])
            
        print(lst)
        if len(digits) == 1:
            return dic[digits]
        ans = []
        if len(digits) == 2:
            lstt = []
            for i in lst[0]:
                lstt.append(i)
                for j in lst[1]:
                    lstt.append(j)
                    ans.append("".join(lstt))
                    lstt.pop()
                lstt.pop()
            return ans
        
        if len(digits) == 3:
            lstt = []
            for i in lst[0]:
                lstt.append(i)
                for j in lst[1]:
                    lstt.append(j)
                    for k in lst[2]:
                        lstt.append(k)
                        ans.append("".join(lstt))
                        lstt.pop()
                    lstt.pop()
                lstt.pop()
            return ans
        
        if len(digits) == 4:
            lstt = []
            for i in lst[0]:
                lstt.append(i)
                for j in lst[1]:
                    lstt.append(j)
                    for k in lst[2]:
                        lstt.append(k)
                        for l in lst[3]:
                            lstt.append(l)
                            ans.append("".join(lstt))
                            lstt.pop()
                        lstt.pop()
                    lstt.pop()
                lstt.pop()
            return ans
        