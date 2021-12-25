class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        reverse = []
        empty = []
        for i in s:
            if i != ')':
                empty.append(i)
            else:
                for i in range(len(empty)):
                    if empty[-1] =='(':
                        empty.pop()
                        empty.extend(reverse)
                        reverse.clear()
                        break
                    else:
                        reverse.append(empty[-1])
                        empty.pop()
           
        tostr = ""
        return tostr.join(empty)
                        