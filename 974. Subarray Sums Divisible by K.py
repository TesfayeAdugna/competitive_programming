class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix = answer = 0
        count = defaultdict(int)
        count[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            answer += count[prefix%k]
            count[prefix%k] += 1
        
        return answer
