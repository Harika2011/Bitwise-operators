def count_flipped_bits(a, b):
    xor = a ^ b  
    count = 0

    while xor:
        count += xor & 1 
        xor >>= 1         

    return count

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

flips_required = count_flipped_bits(num1, num2)
print(f"Number of bits to be flipped to convert {num1} to {num2}: {flips_required}")
