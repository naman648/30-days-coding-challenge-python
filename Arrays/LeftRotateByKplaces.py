def LeftRotate(arr,k):
    n = len(arr)
    if n == 0:
        return arr

    # Calculate effective rotations
    # If d is greater than n, or d is 0, no actual rotation beyond n elements is needed
    k = k % n

    # Slice and concatenate
    # This creates a new list, it does not modify the original in-place
    rotated_arr = arr[k:] + arr[:k]
    return rotated_arr
arr = [1,2,3,4,5,6,7]
k = 3
result = LeftRotate(arr,k)
print(result)