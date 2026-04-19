def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_left(arr, d):
    n = len(arr)
    d = d % n
    
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    
    return arr

arr1 = [12,1,31,85,2,3,53,56323]

arr = [12,1,31,85,2,3,53,56323]
rotate_left(arr, 2)
print("Original array before rotation",arr1)
print("Array after 2 left rotations:", arr)