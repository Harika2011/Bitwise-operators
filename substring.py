def all_subsequences_bitwise(s):
    n = len(s)
    subsequences = []

    for i in range(1, 2 ** n):  
        subseq = ''
        for j in range(n):
            if i & (1 << j):  
                subseq += s[j]
        subsequences.append(subseq)

    return subsequences

text = "abc"
result = all_subsequences_bitwise(text)

print("All Subsequences:")
for seq in result:
    print(seq)
