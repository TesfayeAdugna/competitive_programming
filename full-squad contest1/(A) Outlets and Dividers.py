"""
https://codeforces.com/gym/380981/my
"""
t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    a.sort()
    a = a[::-1]
    summ = 2
    for i in range(len(a)):
        if summ<n:
            summ += a[i]-1
        else:
            print(i)
            break
    else:
        if summ >= n:
            print(len(a))
        else:
            print(-1)