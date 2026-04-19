
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

result = [
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print("Result of Matrix Addition:")
for row in result:
    print(row)