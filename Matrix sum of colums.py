x = [[8, 2, 3],
     [4, 1, 9],
     [1, 4, 8]]

answer = 0

for i in range(len(x)):
    for j in range(len(x[0])):
        answer = answer + x[j][i]
    print(answer, end=" ")
    answer = 0