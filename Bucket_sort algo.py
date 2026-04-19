#divide an array into different buckets
#sort each bucket induvidually using insertion sort - 4 buckets 
#compile it and sort again if needed
#array to be inputed by user 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    buckets = [[] for _ in range(4)]

    maximum = max(arr)
    minimum = min(arr)
    range_val = (maximum - minimum) / 4

    for num in arr:
        index = int((num - minimum) / range_val)
        if index == 4:
            index = 3
        buckets[index].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

print("Original array:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)

