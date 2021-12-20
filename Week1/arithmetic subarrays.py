class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        true = bool('true')
        false = bool('')
        answer = []
        for i in range(m):
            numss = nums[l[i]:r[i]+1]
            numsort = sorted(numss)            
            if len(numsort)<2:
                answer.append(true)
            else:
                interval = numsort[1] - numsort[0]
                
                for j in range(len(numsort)-1):
                    if numsort[j+1] - numsort[j] != interval:
                        answer.append(false)
                        break
                    elif j == len(numsort) - 2:
                        answer.append(true)
                    
        return answer