s = input("Enter a string: ")

rev = ""

for i in range(len(s)-1, -1, -1):
    rev = rev + s[i]

print("Reversed string:", rev)