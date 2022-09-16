class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        
        answer = []
        for i in range(len(nums)+1):
            x = list(combinations(nums, i))
            answer.extend(x)
            
        return answer