class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        ans=0
        while left < right:
            left >>= 1
            right >>= 1
            ans += 1
        left <<= ans
        return left