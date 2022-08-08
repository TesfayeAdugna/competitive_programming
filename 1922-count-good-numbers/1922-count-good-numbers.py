class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        modulo = 10**9 + 7
        
        if n%2 == 1:
            prime = n//2
            even = n//2 + 1
            return (pow(4,prime, modulo) * pow(5,even, modulo))%modulo
        both = n//2
        return (pow(4,both, modulo) * pow(5,both, modulo))%modulo