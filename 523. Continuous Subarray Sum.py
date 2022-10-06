class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        


        prefix = []
        prefixset = set()
        for i in range(len(nums)):
            if not prefix:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1]+nums[i])

        remainderdic = {}
        for i in range(len(prefix)):
            if prefix[i]%k == 0 and i >= 1:
                return True
            if prefix[i]%k in remainderdic and abs(i - remainderdic[prefix[i]%k])>1:
                print(i, remainderdic[prefix[i]%k])
                return True
            if prefix[i]%k not in remainderdic:
                remainderdic[prefix[i]%k] = i
        return False
