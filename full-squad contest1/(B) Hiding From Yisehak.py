"""
https://codeforces.com/gym/380981/my
"""
n = int(input())
for _ in range(n):
    a = int(input())
    h = list(map(int,input().split()))
    stack = []
    for i in range(len(h)):
        while len(stack)>0 and stack[-1] < h[i]:
            stack.pop()
        stack.append(h[i])
        
    print(len(h)-len(stack))
    