def RevArray(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]     # Swapping of elements

#Example usage:
arr = [4,2,1,6,9]
RevArray(arr)
print(arr)