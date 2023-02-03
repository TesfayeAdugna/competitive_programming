class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = path.split('/')
        lst = []
        for i in splitted:
            if i != "":
                lst.append(i)
        stack = []
        for i in lst:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.':
                continue
            else:
                if stack and stack[-1] == '/':
                    stack.append(i)
                else:
                    stack.append('/'+i)
        while stack and stack[-1] == '/':
            stack.pop()
        return "".join(stack) if len(stack)>0 else '/'
            
                
        
        
        
        
        
        
