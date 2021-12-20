#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/counting-valleys/problem
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    sealevel = 0
    valleys = 0
    hills = []
    for i in path:
        if i == 'U':
            sealevel +=1
            hills.append(sealevel)
        else:
            sealevel -=1
            hills.append(sealevel)

    for j in range(steps):
        if hills[j] == 0 and hills[j-1] == -1:
            valleys += 1
            
    return valleys
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
