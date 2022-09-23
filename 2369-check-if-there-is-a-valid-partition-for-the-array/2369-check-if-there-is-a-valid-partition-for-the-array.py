class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        """ 
        0,  1, 2  3  4  5  6
        [4, 4, 4, 4, 4, 5, 6]
        
        [4, 4, 4] [4, 4] [5, 6]
        [4, 4] [4, 4, 4]
        
        (ind1, ind2)
        
        [4, 4] [4, 4, 4] [5, 6]
        [4, 4] [4, 4] [4, 5, 6]
        
        [4, 4, 4] [4, 4] [5, 6]
        [4, 4, 4] [4, 4, 5]

        [4, 4] [4, 5, 6]
        """
        n = len(nums)
        @lru_cache(None)
        def findValidPartition(start, end):
            # base case
            if end >= n:
                return False
            if end - start == 1 and nums[start] != nums[end]:
                return False
            if end - start == 2:
                if (nums[start] != nums[start + 1] or nums[start] != nums[end]) and (nums[start] != nums[start+1]-1 or nums[start] != nums[end]-2):
                    return False
                
            if end == n-1:
                return True

            # recursive calls
            twoElements = findValidPartition(end+1, end+2)
            threeElements = findValidPartition(end+1, end+3)

            return twoElements or threeElements
            
        return findValidPartition(0, 1) or findValidPartition(0, 2)
            
            
            
            
            
            
            
            
            
            
                
            