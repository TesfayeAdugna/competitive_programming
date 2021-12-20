def theatresquare(list1):
    n = list1[0]
    m = list1[1]

    if list1[0] %list1[-1] == 0:
        width = list1[0]//list1[-1]
    if list1[1] %list1[-1] ==0:
        height = list1[1]//list1[-1]
    if list1[0] %list1[-1] !=0:
        width = list1[0]//list1[-1] + 1
    if list1[1] %list1[-1] !=0:
        height = list1[1]//list1[-1] + 1
    total = width * height
    print(total)
    
list1=list(map(int, input().rstrip().split()))
theatresquare(list1)
