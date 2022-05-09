class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        n = pushed.index(popped[0])
        not_pushed = pushed[n+1:]
        pushed = pushed[:n+1]
        i = 0
        while(i<len(popped)):
            if len(pushed)>0 and popped[i] == pushed[-1]:
                pushed.pop()
                if len(pushed)<1 and len(not_pushed)<1:
                    return True
            elif len(not_pushed)>0: # and popped[i] == not_pushed[0]:
                pushed.append(not_pushed[0])
                not_pushed.pop(0)
                if popped[i] == pushed[-1]:
                    pushed.pop()
                    if len(pushed)<1 and len(not_pushed)<1:
                        return True
                else:
                    i-=1
                if len(pushed)<1 and len(not_pushed)<1:
                    return True
            else:
                return False
            
            i+=1
                