def power_set_bitwise(input_set):
    n = len(input_set)
    power_set_result = []

    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(input_set[j])
        power_set_result.append(subset)

    return power_set_result

my_set = [1, 2, 3]
result = power_set_bitwise(my_set)

print("Power Set (using bit manipulation):")
for subset in result:
    print(subset)
