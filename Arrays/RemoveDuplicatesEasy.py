def removeDuplicates(arr):
    i = 0
    while i < len(arr):
        if arr[i] in arr[i+1:]:
            arr.remove(arr[i])
        else:
            i += 1
    return arr
arr = [1,2,3,4,5,5,6,7,7,8,9,10]
print(removeDuplicates(arr))