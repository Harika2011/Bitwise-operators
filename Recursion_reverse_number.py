'''def reverse_number(n, result=0):
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + n % 10)

num = int(input("Enter a positive number: "))
if num > 0:
    reversed_num = reverse_number(num)
    print("Reversed number:", reversed_num)
else:
    print("Please enter a positive number.")'''


def reverseNumber(num):
    if num > 0:
        last = num % 10

        if num // 10 > 0:
            current_number = reverseNumber(num // 10)
            return last * pow(10, len(str(current_number))) + current_number
        else:
            return last
    return num

n = int(input("Enter your number: "))
print("Reversed:", reverseNumber(n))
