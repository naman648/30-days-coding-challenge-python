def MissingNum(arr):
    n = len(arr)
    sum = (n*(n+1))/2
    for i in range(0, n):
        sum -= arr[i]
    return sum
arr = [1,2,3,4,5,6,7,9,10]
print(MissingNum(arr))