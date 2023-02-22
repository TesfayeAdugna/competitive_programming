class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        lst = list(s)
        Answer = 0
        for _ in range(len(lst)):
            flag = False
            i = 0
            while i < len(lst)-1:
                if lst[i] == '0' and lst[i+1] == '1':
                    lst[i] = '1'
                    lst[i+1] = '0'
                    flag = True
                    i += 1
                i += 1

            if flag:
                Answer += 1
            else:
                break
                
        return Answer
