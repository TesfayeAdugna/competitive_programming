class Solution(object):
    def numIdenticalPairs(self, nums):
        init = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    if i < j:
                        init+=1
        return init
