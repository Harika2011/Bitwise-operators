arr_input = input("Enter elements of the array separated by space: ").split()

arr = []
for i in arr_input:
    arr.append(int(i))

duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

if len(duplicates) == 0:
    print("No duplicates found.")
else:
    print("Duplicate elements are:", duplicates)
