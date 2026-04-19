
def selection_sort_one_swap(arr):
    n = len(arr)

    min_index = 0
    for j in range(1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != 0:
        temp = arr[0]
        arr[0] = arr[min_index]
        arr[min_index] = temp

    return arr



arr = [3,5,6,9,8,7]
print(selection_sort_one_swap(arr))
