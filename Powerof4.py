def power4(number):
    if number == 0:
        return 0
    if (number & (~(number - 1))) != number:
        return 0
    if (number - 1) % 3 != 0:
        return 0
    return 1

num = int(input("Enter a number: "))

if power4(num):
    print(f"{num} is a power of 4.")
else:
    print(f"{num} is NOT a power of 4.")
