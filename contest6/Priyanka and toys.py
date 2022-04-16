"""
https://www.hackerrank.com/contests/a2sv3-contest-8/challenges/priyanka-and-toys/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Write your code here
    w.sort()
    output = 0
    start = w[0]
    i=1
    while i<len(w):
        if w[i]-start > 4:
            output += 1
            start = w[i]            
        i+=1
    
    return output + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
