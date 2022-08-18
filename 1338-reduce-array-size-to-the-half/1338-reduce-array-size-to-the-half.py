class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        
        
        
        
        
        
        
        
        n = len(arr)
        count = Counter(arr)
        array = []
        for key in count:
            array.append([count[key], key])
        array.sort(reverse=True)

        i = 0
        acumulate = 0
        while i < len(array) and acumulate < n/2:
            acumulate += array[i][0]
            i += 1
            
        return i