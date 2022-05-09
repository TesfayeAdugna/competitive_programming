class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
    
        
        nextgreater = []
        for i in nums1:
            if i in nums2:
                index = nums2.index(i)
            for j in nums2[index:]:
                if j>i:
                    nextgreater.append(j)
                    break
                elif j == nums2[-1]:
                    nextgreater.append(-1)
                    
        return nextgreater
        
        
     