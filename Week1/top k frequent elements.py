class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        from collections import Counter
        c = Counter(nums)

        output = []
        for i in range(len(c.most_common(k))):
            output.append(c.most_common(k)[i][0])

        return output
            
            