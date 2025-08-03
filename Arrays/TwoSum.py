def twoSum(arr, x):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == x:
                return i+1,j
    return -1
arr = [2, 7, 11, 15, 27, 30]
x = 34
print(twoSum(arr, x))
