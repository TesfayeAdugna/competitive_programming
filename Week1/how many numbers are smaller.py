class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        emptylist=[]
        for i in range(len(nums)):
            emptylist.append(0)
            
        for j in range(len(nums)):
            for k in range(len(nums)):
                if nums[k]<nums[j]:
                    emptylist[j]+=1
        return emptylist