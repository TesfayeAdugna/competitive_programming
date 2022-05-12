"""
https://codeforces.com/contest/1676/my
"""
n = int(input())
for i in range(n):
    a = int(input())
    nums = list(map(int, input().split()))
    
    minn = min(nums)
    output = 0
    for i in nums:
        output+=(i-minn)
    print(output)