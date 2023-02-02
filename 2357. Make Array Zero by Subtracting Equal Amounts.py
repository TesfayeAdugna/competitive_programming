class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        return len(count)-1 if 0 in count else len(count)
