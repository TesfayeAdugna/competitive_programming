class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = []
        for i in range(1, n+1):
            ans.append(bin(i)[2:])
        return int("".join(ans), 2)%(10**9 + 7)