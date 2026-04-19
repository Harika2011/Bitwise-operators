def find_subarray_with_sum(arr, target_sum):
    n = len(arr)
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum == target_sum:
                return arr[start:end+1]
    return None

arr = [15,2,4,8,9,5,10,23]
target_sum = 23
result = find_subarray_with_sum(arr, target_sum)
if result:
    print("Subarray with given sum:", result)
else:
    print("No subarray with the given sum found.")
