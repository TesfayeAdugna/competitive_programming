class Solution:
    def checkValidString(self, s: str) -> bool:

        count_maximum, count_minimum = 0, 0
        for char in s:
            if char == '(':
                count_maximum += 1; count_minimum += 1
            elif char == ')':
                count_maximum -= 1; count_minimum -= 1
            else:
                count_maximum += 1; count_minimum -= 1

            if count_maximum < 0:
                return False
                
            count_minimum = max(count_minimum, 0)

        return count_minimum == 0
