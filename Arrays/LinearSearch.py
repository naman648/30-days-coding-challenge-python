def LinearSearch(arr, x):
    n = len(arr)
    for i in range(0, n):
        if (arr[i] == x):
            return i
        return None
arr = [1,2,6,4,8,9,5]
x = 9
result = LinearSearch(arr, x)
if result == None:
    print("Element is not present in array")
else:
    print("Element is present at index", result)