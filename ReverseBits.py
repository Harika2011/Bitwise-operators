def reverse_bits(n):
    binary = bin(n)[2:]
    
    binary_padded = binary.zfill(32)

    reversed_binary = binary_padded[::-1]

    reversed_number = int(reversed_binary, 2)

    return reversed_number

num = int(input("Enter an integer: "))
result = reverse_bits(num)
print(f"Reversed bits result: {result}")
