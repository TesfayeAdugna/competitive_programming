class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:



        myDict = collections.Counter(nums)
        count = 0
        for i in range(len(nums)):
            sub = target.replace(nums[i],"",1)
            if sub in myDict: 
                if sub == nums[i]: 
                    count += myDict[sub]-1
                else:
                    if (nums[i]+sub)==target:
                        count += myDict[sub]
                        
        return count
