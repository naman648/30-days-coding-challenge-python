# Reverse an Array using Recursion
def RevArray(arr, l, r):      # l: left(from index 0->), r: right(from last index <-)
    # Base
    if l>=r:
        return
    # Swap elements
    arr[l], arr[r] = arr[r], arr[l]
    # Recursive call
    RevArray(arr, l+1, r-1)

#Example usage:
arr = [4,5,9,8,7,2,3,1]
print("Original array: ", arr)

RevArray(arr, 0, len(arr)-1)    # Function call, so the arr --> converted into --> reverse format
print ("Reversed array: ", arr)



    