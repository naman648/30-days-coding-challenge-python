def SecondLarge(arr):
    n = len(arr)
    if n==1:
        return arr
    arr.sort()
    return arr[-2]

arr = [11,7,6,87,54,94,25]
result = SecondLarge(arr)
print(result) 