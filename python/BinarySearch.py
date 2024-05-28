def binary_search(arr, numToFind, low, high):
    if high >= low:
        mid = (high + low) // 2

        #if element is mid then return
        if arr[mid] == numToFind:
            return mid
        #if element is smaller than mid then search the left subarray
        elif numToFind < arr[mid]:
            return binary_search(arr, numToFind,low, mid-1)
        
        #else search teh right subarray
        else:
            return binary_search(arr, numToFind, mid+1, high)
    else:
        return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, x , 0, len(arr)-1)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")