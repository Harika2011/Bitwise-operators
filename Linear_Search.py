arr_input = input("Enter elements of the array separated by space: ").split()

arr = []
for i in arr_input:
    arr.append(int(i))

x = int(input("Enter the element to search: "))

found = False
for i in range(len(arr)):
    if arr[i] == x:
        print(f"Element {x} found at position {i+1}.")
        found = True
        break

if not found:
    print(f"Element {x} not found in the array.")
