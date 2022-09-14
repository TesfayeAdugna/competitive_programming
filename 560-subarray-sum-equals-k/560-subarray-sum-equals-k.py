class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        
        res = 0
        dic = defaultdict(int)
        dic[0]+=1
        for i in range(len(nums)):
            if i > 0: nums[i] += nums[i-1]
            
            if nums[i] - k not in dic:
                dic[nums[i]] += 1
            else:
                res += dic[nums[i]-k]
                dic[nums[i]] += 1
                    
        return res