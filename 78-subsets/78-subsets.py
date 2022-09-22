class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer, index, n = [], 0, len(nums)
        while index < (1<<n):
            subset = []
            for i in range(32):
                if index & (1<<i): subset.append(nums[i])
            answer.append(subset)
            index += 1
        return answer