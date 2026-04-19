def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 5, 3, 3, 2]  
odd_occurrence = find_odd_occurrence(arr)
print("Element occurring odd number of times:", odd_occurrence)
