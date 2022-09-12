class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
            
        for i in range(len(nums)):
            if (target-nums[i]) in dic:
                if i != dic[target-nums[i]]:
                    return [i, dic[target-nums[i]]]