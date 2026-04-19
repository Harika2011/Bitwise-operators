def find_two_odd_occurring(arr):
    xor = 0
    for num in arr:
        xor ^= num

    rightmost_set_bit = xor & -xor

    res1 = 0
    res2 = 0

    for num in arr:
        if num & rightmost_set_bit:
            res1 ^= num
        else:
            res2 ^= num

    return res1, res2

arr = [4, 3, 4, 4, 4, 5, 5, 3, 1, 2, 1, 3, 4, 5, 6, 7]

result = find_two_odd_occurring(arr)
print("The two odd occurring numbers are:", result)
