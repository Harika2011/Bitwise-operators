arr = [3, 3, 1, 1, 1, 8, 3, 6, 1, 7, 8]

freq = {}
index = {}

for i in range(len(arr)):
    if arr[i] not in freq:
        freq[arr[i]] = 1
        index[arr[i]] = i
    else:
        freq[arr[i]] += 1

sorted_arr = sorted(arr, key=lambda x: (-freq[x], index[x]))

print("Original array:", arr)
print("Sorted by frequency and index:", sorted_arr)
