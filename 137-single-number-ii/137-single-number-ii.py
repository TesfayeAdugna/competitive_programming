class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        one, two = 0, 0
        for a in nums:
            one = (one^a)&(~two)
            two = (two^a)&(~one)
        return one