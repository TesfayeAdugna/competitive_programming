class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        summ, answer, even = 0, [], set()
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                summ += nums[i]
                even.add((nums[i], i))
        
        for querie in queries:
            if (nums[querie[1]], querie[1]) in even:
                summ -= nums[querie[1]]
                even.remove((nums[querie[1]], querie[1]))
                
            nums[querie[1]] += querie[0]
            
            if nums[querie[1]]%2 == 0:
                summ += nums[querie[1]]
                even.add((nums[querie[1]], querie[1]))
                
            answer.append(summ)
            
        return answer