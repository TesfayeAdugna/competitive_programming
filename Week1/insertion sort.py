#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    m = arr[n-1]
    if n==2:
        temp=arr[1]
        if arr[1]<arr[0]:
            arr[1]=arr[0]
            for j in arr:
                print(j, end=" ")
            print()
            arr[0]=temp
            for j in arr:
                print(j, end=" ")
            print()
    else:
        for i in range(n-1):
            if arr[n-i-2]>m:
                arr[n-i-1] = arr[n-2-i]
                for j in arr:
                    print(j, end=" ")
                print()
            else:
                arr[n-1-i]=m
                for j in arr:
                    print(j, end=" ")
                print()
                break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
