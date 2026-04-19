def recursive_array_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursive_array_sum(arr[1:])


numbers = [5, 8, 2, 10, 3]
total = recursive_array_sum(numbers)
print("Input array:", numbers)
print("Sum of elements:", total)
