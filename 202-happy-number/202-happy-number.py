class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            temp_n = 0
            while n > 0:
                temp_n += pow(n%10, 2)
                n //= 10
            n = temp_n
        return n == 1