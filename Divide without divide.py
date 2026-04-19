
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("Error: Division by zero is not allowed.")
else:
    quotient = 0
    negative = False

    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        negative = True

    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if negative:
        quotient = -quotient

    print("Quotient =", quotient)
    print("Remainder =", dividend)
