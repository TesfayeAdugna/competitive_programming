class Solution:
    def op(self,a,c,b):
        if a == '*':
            return int(b) * int(c)
        if a == '/':
            return int(c) // int(b)
        if a == '+':
            return int(b) + int(c)
        if a == '-':
            return int(c) - int(b)
    def calculate(self, s: str) -> int:
        s.strip()
        hold = []
        hold1 = []
        m = ''
        for i in s:
            if i not in '+-*/':
                m += i
            else:
                hold.append(int(m))
                hold.append(i)
                m = ''
        hold.append(int(m))
        for i in range(len(hold)-1):
            if str(hold[i]) in '*/':
                hold[i+1] = self.op(hold[i],hold1.pop(),hold[i+1])

            else:
                hold1.append(hold[i])
        hold1.append(hold[-1])
        for i in range(len(hold1)-1):
            if str(hold1[i]) in '+-':
                hold1[i+1] = self.op(hold1[i],hold1[i-1],hold1[i+1])
        return hold1[-1]    
    