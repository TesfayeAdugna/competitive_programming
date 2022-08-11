class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        
        
        
        
        
        if len(nums) == 1: return nums[0]
        dic1 = {}
        dic2 = {}
        def robber(index, flag):
            if flag and index in dic1:
                return dic1[index]
            if not flag and index in dic2:
                return dic2[index]
            
            if index >= len(nums)-2:
                if not flag and index == len(nums)-1:
                    return nums[index]-nums[0] if nums[index] > nums[0] else 0
                return nums[index]
            
            left = nums[index] + robber(index+2, flag)
            right = nums[index] + robber(index+3, flag) if index < len(nums)-3 else 0
            if flag:
                dic1[index] = max(left, right)
            if not flag:
                dic2[index] = max(left, right)
                
            return dic1[index] if flag else dic2[index]
        
        return max(robber(0, False), robber(1, True))