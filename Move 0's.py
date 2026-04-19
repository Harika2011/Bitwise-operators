def move_zeros_to_end(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr

arr = [1,0,3,6,0,0,0,2,355,0,72]
result = move_zeros_to_end(arr)
print("After moving zeros to end:", result)
