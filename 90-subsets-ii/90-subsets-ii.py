class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        
        answer, index, n = set(), 0, len(nums)
        while index < (1<<n):
            subset = []
            for i in range(32):
                if index & (1<<i): subset.append(nums[i])
            subset.sort()
            answer.add(tuple(subset))
            index += 1
        return list(answer)