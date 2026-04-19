def is_sorted(arr, index=0):
    if index == len(arr) - 1 or len(arr) == 0:
        return True

    if arr[index] > arr[index + 1]:
        return False

    return is_sorted(arr, index + 1)

arr = [10, 90, 70, 95,35]
if is_sorted(arr):
    print("The array is sorted.👏🏻")
else:
    print("The array is not sorted.🙁")
