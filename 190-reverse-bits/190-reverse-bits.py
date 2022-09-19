class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        
        n = bin(n)[2:]
        lst = list(n)
        lst = lst[::-1]
        while len(lst)<32:
            lst.append('0')
            
        summ = 0
        for i in range(len(lst)):
            summ += (2**i) * int(lst[-i-1])
        
        return summ
        
        
#         rev = 0
#         while n:
#             rev <<= 1
#             rev += n & 1
#             n >>= 1
#         return rev