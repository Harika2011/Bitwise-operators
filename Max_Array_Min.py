def find_max_min(arr):
    if not arr:
        return None, None  

    max_element = arr[0]
    min_element = arr[0]

    for num in arr[1:]:
        if num > max_element:
            max_element = num
        elif num < min_element:
            min_element = num

    return max_element, min_element

array = [12,1234,-45,67,1]
maximum, minimum = find_max_min(array)

print("Maximum element:", maximum)
print("Minimum element:", minimum)