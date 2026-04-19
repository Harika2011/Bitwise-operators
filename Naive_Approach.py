def find_pair(arr, X):
    n = len(arr)
    found = False

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == X:
                print("Pair found:", arr[i], arr[j])
                found = True

    if not found:
        print("No pair found")


arr = [2, 7, 11, 15,19,21]
X = 9
find_pair(arr, X)
