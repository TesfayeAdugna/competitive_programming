class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        operand = ['+', '*', '/', '-']
        empty = []
        for i in tokens:
            if i not in operand:
                empty.append(int(i))
            elif i in operand and i == operand[0]:
                sam = empty[-1] + empty[-2]
                empty.pop()
                empty.pop()
                empty.append(sam)
            elif i in operand and i == operand[1]:
                sam = empty[-1] * empty[-2]
                empty.pop()
                empty.pop()
                empty.append(sam)
            elif i in operand and i == operand[2]:
                sam = math.trunc(empty[-2] / empty[-1])
                empty.pop()
                empty.pop()
                empty.append(sam)
            elif i in operand and i == operand[3]:
                sam = empty[-2] - empty[-1]
                empty.pop()
                empty.pop()
                empty.append(sam)
        return empty[0]
              
              