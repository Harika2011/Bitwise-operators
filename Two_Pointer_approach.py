def find_pair(arr, X):
    arr.sort()          
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == X:
            print("Pair found:", arr[left], arr[right])
            return
        elif current_sum < X:
            left += 1
        else:
            right -= 1

    print("No pair found")


arr = [6, 4, 21, 12]
X = 10
find_pair(arr, X)
