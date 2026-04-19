def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        
        arr[i], arr[max_index] = arr[max_index], arr[i]

digits = [3,30,34,5,9]

print("Original list:", digits)
selection_sort(digits)
print("Sorted list:",digits)
print("Largest number in the list:",digits[0])