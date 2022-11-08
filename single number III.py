class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        xor = 0
        for num in nums:
            xor ^= num

        firstbit = xor & (xor-1) ^ xor
        num1 = 0
        for num in nums:
            if num & firstbit:
                num1 ^= num

        return [num1, num1^xor] 
