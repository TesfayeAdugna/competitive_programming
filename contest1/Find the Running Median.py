"""
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
Example

Sorted          Median
[7]             7.0
[3, 7]          5.0
[3, 5, 7]       5.0
[2, 3, 5, 7]    4.0
Each of the median values is stored in an array and the array is returned for the main function to print.

Note: Add formatting to the print statement.

Function Description
Complete the runningMedian function in the editor below.

runningMedian has the following parameters:
- int a[n]: an array of integers

Returns
- float[n]: the median of the array after each insertion, modify the print statement in main to get proper formatting.

Input Format

The first line contains a single integer, , the number of integers in the data stream.
Each line  of the  subsequent lines contains an integer, , to be inserted into the list.

Constraints

Sample Input

STDIN   Function
-----   --------
6       a[] size n = 6
12      a = [12, 4, 5, 3, 8, 7]
4
5
3
8
7
Sample Output

12.0
8.0
5.0
4.5
5.0
6.0
Explanation

There are  integers, so we must print the new median on a new line as each integer is added to the list:


"""

#!/bin/python3
import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
maxheap = []
minheap = []

def insert(val):
    heapq.heappush(maxheap,-1*val)
    if len(maxheap)-len(minheap) == 2:
        heapq.heappush(minheap,-1*heapq.heappop(maxheap))
    if len(minheap)>0 and -1*maxheap[0] > minheap[0]:
        heapq.heappush(minheap,-1*heapq.heappop(maxheap))
        heapq.heappush(maxheap,-1*heapq.heappop(minheap))
        
def getmedian():
    len1 = len(maxheap)
    len2 = len(minheap)
    if len1==len2:
        return (-1*maxheap[0] + minheap[0]) / 2.0
    return -1*maxheap[0] * 1.0
    
def runningMedian(a):
    # Write your code here
    result = []
    for n in a:
        insert(n)
        result.append(getmedian())
            
    return result

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
