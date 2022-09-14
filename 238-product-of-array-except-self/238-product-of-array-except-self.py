class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        prefix = []
        suffix = []
        for i in range(len(nums)):
            if not prefix or not suffix:
                prefix.append(nums[i])
                suffix.append(nums[-i-1])
            else:
                prefix.append(prefix[-1] * nums[i])
                suffix.append(suffix[-1] * nums[-i-1])
                
        suffix = suffix[::-1]
        answer = []
        for i in range(len(nums)):
            pre = 1
            post = 1
            if i > 0:
                pre = prefix[i-1]
            if i < len(nums)-1:
                post = suffix[i+1]
                
            answer.append(pre*post)
        return answer