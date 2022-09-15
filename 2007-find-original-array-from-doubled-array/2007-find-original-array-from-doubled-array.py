class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        answer = []
        changed.sort()
        count = Counter(changed)
        
        for i in range(len(changed)):
            if changed[i]%2 == 0 and changed[i]//2 in count:
                if changed[i] != 0 and count[changed[i]]>0 and count[changed[i]//2]>0:
                    count[changed[i]] -= 1
                    count[changed[i]//2] -= 1
                    answer.append(changed[i]//2)
                else:
                    if changed[i] == 0 and count[changed[i]]>1:
                        count[changed[i]] -= 2
                        answer.append(changed[i])
                        
        return answer if len(changed)%2==0 and len(answer) == len(changed)//2 else []