def power2(number):
    if number == 0:
        return 0
    if (number & (~(number - 1))) == number:
        return 1
    return 0

num = int(input("Enter a number: "))

if power2(num):
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is NOT a power of 2.")
