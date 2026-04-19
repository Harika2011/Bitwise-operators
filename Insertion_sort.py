a = [10, 5, 13, 8, 2]

for i in range(1, len(a)):
    j = i
    while j > 0 and a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1

print("Sorted list:", a)
