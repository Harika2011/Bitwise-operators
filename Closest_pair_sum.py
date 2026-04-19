def pair_closest_to_x(arr, X):
    arr = sorted(set(arr))
    
    left = 0
    right = len(arr) - 1
    
    closest_sum = float('inf')
    result_pair = None

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if abs(X - current_sum) < abs(X - closest_sum):
            closest_sum = current_sum
            result_pair = (arr[left], arr[right])
        
        if current_sum < X:
            left += 1
        else:
            right -= 1

    return result_pair, closest_sum


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))
    X = int(input("Enter target value X: "))

    pair, closest_sum = pair_closest_to_x(arr, X)

    print("Unique sorted array:", sorted(set(arr)))
    print("Pair closest to X:", pair)
    print("Closest sum:", closest_sum)
