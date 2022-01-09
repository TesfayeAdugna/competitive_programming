class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
                                 
        changed = sorted(changed)
        counted = dict(Counter(changed))

        if len(changed)%2 == 1:
            return []
        
        mm = len(changed)//2
        original = []

        original = [0] * (changed.count(0)//2)

        for i in counted:
            if counted[i] == 0 or i == 0:
                continue
            elif i*2 not in counted:
                return []
            elif counted[2*i] >= counted[i]:
                counted[2*i] = counted[2*i] - counted[i]
                original.extend([i]*counted[i])
            else:
                return []
            if len(original)>=mm:
                return original
        return original
            