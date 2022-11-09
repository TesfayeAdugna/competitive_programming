class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        duplicate, missing = 0, 0
        for key in range(1, len(nums)+1):
            if key not in c:
                missing = key
            elif c[key] == 2:
                duplicate = key
        return [duplicate, missing]
            
