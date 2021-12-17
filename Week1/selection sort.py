class Solution: 
    def select(self, arr, i):
        # code here 
        for x in range(len(arr)):
            i = arr[x]
            for y in range(x,len(arr)):
                if i>arr[y]:
                    i=arr[y]
            index1 = arr.index(i)
            arr[index1], arr[x] = arr[x], arr[index1]
            return i
    def selectionSort(self, arr,n):
        #code here
        for x in range(n):
            i = arr[x]
            for y in range(x,n):
                if i>arr[y]:
                    i=arr[y]
            temp =arr[x]
            arr[x]=i
            for k in range(x+1,len(arr)):
                if i == arr[k]:
                    arr[k]=temp
                    break