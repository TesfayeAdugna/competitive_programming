class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        
        ans = []
        flag = a > b
        while a > 0 or b > 0:
            if flag:
                if a > b and a >= 2:
                    ans.append("aa")
                    a -= 2
                else:
                    ans.append("a")
                    a -= 1
                flag = not flag
            else:
                if b > a and b >= 2:
                    ans.append("bb")
                    b -= 2
                else:
                    ans.append("b")
                    b -= 1
                flag = not flag
                    
        return "".join(ans)
        