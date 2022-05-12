"""
https://codeforces.com/contest/1676/my
"""
n = int(input())
for i in range(n):
    a = str(input())
    
    count1 = 0
    count2 = 0
    
    for i in range(3):
        count1 += int(a[i])
    for j in range(3,6):
        count2+= int(a[j])
    if count1 == count2:
        print("YES")
    else:
        print("NO")