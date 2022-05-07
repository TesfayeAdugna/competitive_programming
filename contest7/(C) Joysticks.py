"""
https://codeforces.com/gym/380193/my
"""
arr = list(map(int,input().split()))
 
 
i = 0
while arr[0] > 0 and arr[1] > 0:
    if arr[0]==1 and arr[1]==1:
        break
    if arr[0] <= arr[1]:
        arr[0] += 1
        arr[1] -= 2
    else:
        arr[1] += 1
        arr[0] -= 2
    i+=1
 
print(i)