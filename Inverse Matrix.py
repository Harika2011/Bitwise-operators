a = 3
b = 1
c = 4
d = 2

det = a*d - b*c

if det == 0:
    print("Inverse does not exist")
else:
    inv = [
        [d/det, -b/det],
        [-c/det, a/det]
    ]

    print("Inverse Matrix:")
    for row in inv:
        print(row)