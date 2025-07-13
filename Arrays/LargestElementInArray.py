def largeElement(arr):
    n = len(arr)
    if n==1:
        return arr
    large = arr[0]
    for i in range(1,n):
        if arr[i] > large:
            large = arr[i]
    return large

arr = [4,1,9,5,7]
result = largeElement(arr)
print(result)
