#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    n=len(a)
    count=0
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                count+=1
    print("Array is sorted in", count ,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)