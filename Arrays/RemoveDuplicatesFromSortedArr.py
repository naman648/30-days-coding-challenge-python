def removeDuplicates(arr):
    if not arr:
        return 0
    n = len(arr)
    k = 1  # Pointer for the next unique element's position
    for i in range(1, n):
        if arr[i] != arr[k-1]:
            arr[k] = arr[i]
            k+=1
    return k
# Example usage:
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
result = removeDuplicates(arr)
print(result)
print(arr)
