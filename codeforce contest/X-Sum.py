"""
https://codeforces.com/contest/1676/my
"""
t = int(input())
for i in range(t):
    n,m = list(map(int, input().split()))
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
        
    dic1 = {}
    dic2 = {}
    
    for i in range(n):
        for j in range(m):
            if i+j in dic1:
                dic1[i+j] += lst[i][j]
            else:
                dic1[i+j] = lst[i][j]
            if i-j in dic2:
                dic2[i-j] += lst[i][j]
            else:
                dic2[i-j] = lst[i][j]
 
    sumlist = []
    for i in range(n):
        for j in range(m):
            sumlist.append(dic1[i+j] + dic2[i-j] - lst[i][j])
    print(max(sumlist))