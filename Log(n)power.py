def power(x, y):
    result = 1
    base = x
    exponent = y

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2

    return result

x = int(input("Enter the base (x): "))
y = int(input("Enter the exponent (y): "))

print(x, "raised to the power", y, "is", power(x, y))
