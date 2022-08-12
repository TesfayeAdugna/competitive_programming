class Solution:
    def decodeString(self, s: str) -> str:
        
        
        
        
        
        def decode(s):
            Ans = ""
            i = 0
            while i < len(s):
                if s[i].isdigit():
                    j = i
                    while s[i].isdigit():
                        i += 1
                        
                    temp = int(s[j:i])
                    
                    stack = [s[i]]
                    i+=1
                    start = i
                    while stack:
                        if s[i] == "[":
                            stack.append(s[i])
                        elif s[i] == "]":
                            stack.pop()
                        i+=1
                    Ans += decode(s[start:i-1]) * temp
                    
                else:
                    Ans += s[i]
                    i += 1
                    
            return Ans
        
        
        return decode(s)