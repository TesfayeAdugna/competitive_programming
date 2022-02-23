"""
Given an array of size N. The task is to sort the array elements by completing functions heapify() and buildHeap() which are used to implement Heap Sort.

Example 1:

Input:
N = 5
arr[] = {4,1,3,9,7}
Output:
1 3 4 7 9
Explanation:
After sorting elements
using heap sort, elements will be
in order as 1,3,4,7,9.
Example 2:

Input:
N = 10
arr[] = {10,9,8,7,6,5,4,3,2,1}
Output:
1 2 3 4 5 6 7 8 9 10
Explanation:
After sorting elements
using heap sort, elements will be
in order as 1, 2,3,4,5,6,7,8,9,10.

Your Task :
You don't have to read input or print anything. Your task is to complete the functions heapify(), buildheap() and heapSort() where heapSort() and buildheap() takes the array and it's size as input and heapify() takes the array, it's size and an index i as input. Complete and use these functions to sort the array using heap sort algorithm.
Note: You don't have to return the sorted list. You need to sort the array "arr" in place.

Expected Time Complexity: O(N * Log(N)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
1 ≤ arr[i] ≤ 106
"""

#User function Template for python3
class Solution:
    def leftchild(self,index):
        return 2*index + 1
    def rightchild(self,index):
        return 2*index + 2
    def parent(self, index):
        return (index-1)//2
    
    #Heapify function to maintain heap property.
    def upheap(self,arr,n,i):
        if i>0 and arr[i]< arr[self.parent(i)]:
            arr[i],arr[self.parent(i)] = arr[self.parent(i)], arr[i]
            i = self.parent(i)
            self.upheap(arr,n,i)
            
    def downheap(self, arr,n,i):
        if self.leftchild(i) >= n:
            return
        else:
            minimum = self.leftchild(i)
            if self.rightchild(i)<n and arr[self.rightchild(i)] < arr[self.leftchild(i)]:
                minimum = self.rightchild(i)
                
            if arr[i] > arr[minimum]:
                arr[minimum],arr[i] = arr[i],arr[minimum]
                i = minimum
                self.downheap(arr,n,i)
                    
    def heapify(self,arr, n, i):
        # code herez
        self.upheap(self,arr,n,i)
        self.downheap(self,arr,n,i)
                
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n):
            self.upheap(arr,n,i)
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)

        li = n-1
        for i in range(n):
            arr[li],arr[0] = arr[0], arr[li]
            self.downheap(arr,li,0)
            li -= 1
            
        for i in range(len(arr)//2):
            arr[i], arr[-i-1] = arr[-i-1], arr[i]


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends