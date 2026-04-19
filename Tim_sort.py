#divide it chunks and then each chunk should have a fixed size 
#use insertion sort
#merge it and sort again if needed 
#array to be entered by user


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def tim_sort(arr):
    n = len(arr)
    RUN = 4   

    for i in range(0, n, RUN):
        insertion_sort(arr, i, min(i + RUN - 1, n - 1))

    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                arr[left:right + 1] = sorted(arr[left:right + 1])

        size *= 2


arr = list(map(int, input("Enter the array elements: ").split()))
print("Original array:", arr)

tim_sort(arr)
print("Sorted array:", arr)


