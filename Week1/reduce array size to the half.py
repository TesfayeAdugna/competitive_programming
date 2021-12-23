class Solution:
    def minSetSize(self, arr: List[int]) -> int:
         
        k = len(arr)
        from collections import Counter
        c = Counter(arr)
        nums = []
        for i in c.most_common(k):
            num = [i[0]] * i[1]
            nums.extend(num)
        arrsort = nums
        output = 1
        length = len(arr)
        n = length//2
        newarr = []
        for i in range(n, length):
            if arrsort[i] != arrsort[i-1]:
                newarr = arrsort[0:i]
                break   
            elif i == length-1:
                for i in range(n,0,-1):
                    if arrsort[i] != arrsort[i-1]:
                        newarr = arrsort[i:]
                        break
        if len(newarr)>=1:
            length2 = len(newarr)
        else:
            return 1
        for j in range(length2-1):
            if newarr[j+1]!=newarr[j]:
                output +=1
        return output