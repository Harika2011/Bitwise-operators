def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        if left_sum == (total_sum - left_sum - num):
            return i  
        left_sum += num

    return -1  

arr = [-7, 1, 5, 2, -4, 3, 0]
index = find_equilibrium_index(arr)

if index != -1:
    print(f"Equilibrium index found at position: {index}")
else:
    print("No equilibrium index found.")
