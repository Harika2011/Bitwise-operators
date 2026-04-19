
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("\nMethod 1: Using arithmetic operations")

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

a = int(input("\nEnter the first number again (a): "))
b = int(input("Enter the second number again (b): "))

print("\nMethod 2: Using XOR bitwise operator")

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)
