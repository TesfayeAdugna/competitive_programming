class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        away, here, result, dictionary = 0, 0, 0, {}
        for num in nums:
            dictionary[num] = dictionary.get(num,0) + 1
            if len(dictionary) > k:
                del dictionary[nums[here]]
                here += 1
                away = here
            if len(dictionary) ==  k:
                while dictionary[nums[here]] > 1:
                    dictionary[nums[here]] -= 1
                    here += 1
                result += here - away + 1
        return result
