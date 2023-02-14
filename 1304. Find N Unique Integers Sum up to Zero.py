class Solution:
    def sumZero(self, n: int) -> List[int]:



        result = []
        total_sum = 0
        if n%2 == 1:
            result.append(0)
            n -= 1

        for i in range(1, n//2+1):
            result.append(i)
            result.append(-i)

        return result
        


