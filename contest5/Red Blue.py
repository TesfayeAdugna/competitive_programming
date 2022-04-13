"""
https://codeforces.com/gym/377316/problem/A
"""


num = int(input())
for i in range(num):
    n = int(input())
    red = str(input())
    blue = str(input())
    
    r = 0
    b = 0
    for i in range(n):
        if int(red[i]) > int(blue[i]):
            r += 1
        elif int(red[i]) < int(blue[i]):
            b += 1
    if r>b:
        print("RED")
    elif r<b:
        print("BLUE")
    else:
        print("EQUAL")