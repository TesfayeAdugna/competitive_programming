class Solution:
    #https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/
    def maxCoins(self, piles: List[int]) -> int:
        
        maxcoin = 0
        pilesort = sorted(piles)
        for i in range(len(pilesort)//3):
            maxcoin += pilesort[(-2 * i)-2]
        return maxcoin