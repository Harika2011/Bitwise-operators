
A = [
    [9, 8, 7],
    [6, 5, 4]
]

B = [
    [1, 2, 3],
    [4, 5, 6]
]

result = [
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - B[i][j]

print("Result of Matrix Subtraction:")
for row in result:
    print(row)