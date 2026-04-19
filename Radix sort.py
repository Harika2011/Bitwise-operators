#sort the numbers digit by digit
#either units,tens,hundreds
#use counting sort method for each digit
#able to use large number of digits 


def counting_sort_by_digit(arr, exp):
    n = len(arr)

    output = [0] * n
    count = [0] * 10   

    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1   

    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10



n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

radix_sort(arr)

print("Sorted list:", arr)
