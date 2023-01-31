class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r, finalAns = 0,  k-1, 101
        while r < len(blocks):
            finalAns = min(Counter(blocks[l:r+1])['W'] , finalAns)
            l, r = l+1, r+1
        return finalAns
