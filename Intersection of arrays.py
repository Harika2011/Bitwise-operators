def intersection_sorted_arrays(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result


arr1 = [1, 2, 4, 5, 6, 8, 10]
arr2 = [2, 3, 5, 7, 10, 15]

intersection = intersection_sorted_arrays(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Intersection:", intersection)

if intersection:
    print("Largest number in the intersection:", intersection[-1])
else:
    print("No common elements found")
