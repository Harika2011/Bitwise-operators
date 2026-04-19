def find_union(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue
        if j > 0 and arr2[j] == arr2[j - 1]:
            j += 1
            continue

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if i == 0 or arr1[i] != arr1[i - 1]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if j == 0 or arr2[j] != arr2[j - 1]:
            result.append(arr2[j])
        j += 1

    return result


arr1 = [1,2,8,9]
arr2 = [2,3,5,7]

print("Union:", find_union(arr1, arr2))