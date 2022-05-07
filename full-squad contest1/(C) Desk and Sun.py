"""
https://codeforces.com/gym/380981/my
"""
n,m = list(map(int,input().split()))
dp = {}
for _ in range(n):
    chair = tuple(map(int,input().split()))
    if chair in dp:
        dp[chair] += 1
    else:
        dp[chair] = 1
 
for _ in range(m):
    hour = list(map(int,input().split()))
    count = 0
    for i in range(hour[0],hour[2]+1):
        for j in range(hour[1],hour[3]+1):
            if (i,j) in dp:
                count += dp[(i,j)]
    print(count)
        