import time

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)

    lps = [0] * m
    j = 0

    i = 1
    length = 0
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    i = j = 0
    positions = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


def rabin_karp(text, pattern):
    d = 256
    q = 101

    m = len(pattern)
    n = len(text)

    p = 0
    t = 0
    h = 1
    positions = []

    for _ in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                positions.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return positions


text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

start = time.perf_counter()
kmp_result = kmp_search(text, pattern)
kmp_time = time.perf_counter() - start

start = time.perf_counter()
rk_result = rabin_karp(text, pattern)
rk_time = time.perf_counter() - start

print("\nKMP Positions:", kmp_result)
print("KMP Time:", kmp_time, "seconds")

print("\nRabin-Karp Positions:", rk_result)
print("Rabin-Karp Time:", rk_time, "seconds")
