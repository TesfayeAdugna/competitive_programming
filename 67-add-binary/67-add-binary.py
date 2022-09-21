class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        value_a = int(a, 2)
        value_b = int(b, 2)
        
        return bin(value_a + value_b)[2:]