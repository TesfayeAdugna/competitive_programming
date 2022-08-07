class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[1] * 5] + [[0] * (5) for _ in range(n - 1)]
        moduler = math.pow(10, 9) + 7
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % moduler
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % moduler
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % moduler
            dp[i][3] = (dp[i - 1][2]) % moduler
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % moduler
            
        return int(sum(dp[-1]) % moduler)