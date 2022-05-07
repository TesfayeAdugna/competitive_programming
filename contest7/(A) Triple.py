"""
https://codeforces.com/gym/380193/my
"""
from collections import Counter
total = int(input())
for _ in range(total):
    each = int(input())
    arr = list(map(int,input().split()))
    
    dic = {}
    for i in arr:
        if i in dic:
            dic[i]+=1
            if dic[i]>=3:
                print(i)
                break
        else:
            dic[i] = 1
    else:
        print(-1)
