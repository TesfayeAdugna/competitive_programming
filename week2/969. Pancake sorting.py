class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
           
        output = []
        length = len(arr)
        i = 0
        while(length>1):
            length = len(arr) - i
            if max(arr[:length]) == arr[length-1]:
                i += 1
                continue
            else:
                k = arr.index(max(arr[:length]))
                arr = arr[k::-1] + arr[k+1:]
                output.append(k+1)
                arr = arr[length-1::-1] + arr[length:]
                output.append(length)
                i += 1
        return output