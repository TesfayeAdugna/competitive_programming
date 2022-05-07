"""
https://codeforces.com/gym/380193/my
"""

arr = list(map(int,input().split()))
 
output = 0
v = arr[1]
l = arr[0]-1
 
i = 1
summ = 0
while summ < l:
    if i == 1 and arr[1]<arr[0]:
        output += v*i
        summ+=v
    elif i == 1 and arr[1]>=arr[0]:
        output += l
        summ += l
    else:
        output += i
        summ += 1
    i+=1
    
print(output)