class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + nums[i - 1]
        res = len(nums) + 1
        Q = collections.deque()
        for i in range(len(dp)):
            while Q and dp[i] - dp[Q[0]] >= k:
                res = min(res, i - Q.popleft())
            while Q and dp[i] < dp[Q[-1]]:
                Q.pop() # pop right
            Q.append(i)
        return res if res != len(nums)+1 else -1
