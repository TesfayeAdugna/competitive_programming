class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
   
        
        if digits[-1] == 9:
            i = 0
            while i < len(digits) and digits[-i-1] == 9:
                digits[-i-1] = 0
                i+=1
            if i > len(digits) -1:
                digits = [1] + digits
            else:
                digits[-i-1] += 1
        else:
            digits[-1] += 1
        
        return digits
