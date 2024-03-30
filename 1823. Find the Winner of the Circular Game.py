class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # [1, 2, 3, 4, 5], k = 2
        # [1, 3, 4, 5]
        # [1, 3, 5]
        # [3, 5]
        # [3]

        arr = [i for i in range(1, n+1)]
        start = 0
        while len(arr) > 1:
            to_be_removed = (start + k - 1)%len(arr) # 2 + 2 - 1 = 3%3 = 0
            arr.pop(to_be_removed)
            start = to_be_removed

        return arr[0]
