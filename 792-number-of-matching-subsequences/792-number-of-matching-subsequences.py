class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        
        
        dic = defaultdict(list)
        output = 0
        for i in range(len(s)):
            dic[s[i]].append(i)
        
        def binarySearch(lst,i):
            left,right = 0,len(lst)
            while left<right:
                mid = (left+right)//2
                if i<lst[mid]:
                    right=mid
                else:
                    left=mid+1
            return left
        for word in words:
            prev = -1
            found = True
            for c in word:
                tmp = binarySearch(dic[c],prev)
                if tmp == len(dic[c]):
                    found = False
                    break
                else:
                    prev = dic[c][tmp]
            if found:
                output += 1
                
        return output