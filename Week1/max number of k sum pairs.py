class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/
        nums = sorted(nums)
        begin = 0
        end = len(nums)-1
        operations = 0
        while(begin < end):
            if nums[begin] + nums[end] > k:
                end -= 1
            elif nums[begin] + nums[end] < k:
                begin +=1
            else:
                begin +=1
                end -= 1
                operations += 1

        return operations