class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        print("2&4: ", 2 & 2)
        n = len(nums)
        answer = []
        index = 0
        while index < (1<<n):
            subset = []
            for i in range(32):
                if index & (1<<i):
                    subset.append(nums[i])
            answer.append(subset)
            index += 1
            
        return answer