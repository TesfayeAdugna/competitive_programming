"""
https://codeforces.com/gym/377316/problem/B
"""
n = int(input())
arr =  list(map(int, input().split())) 
 
coin = 0
negative = 0
positive = 0
zero = 0
for i in range(n):
    if arr[i] <= -1:
        coin += (-1 - arr[i])
        arr[i] = -1
        negative += 1
    elif arr[i] >= 1:
        coin += (arr[i] - 1)
        arr[i] = 1
        positive += 1
    else:
        zero+=1
            
while zero>0:
    if negative % 2 != 0:
        negative += 1
        coin += 1
    else:
        positive += 1
        coin += 1
    zero -= 1
    
if negative % 2 != 0:
    coin += 2
print(coin)
