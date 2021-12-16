def dominopiling(arr):
    max_number_of_dominos = (arr[0]*arr[1])//2
    print(max_number_of_dominos)
arr=list(map(int, input().rstrip().split()))
dominopiling(arr)