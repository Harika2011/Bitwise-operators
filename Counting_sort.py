#user enters some values 
#smallest value out of a list of numbers- how many times that occurs 
#frequency method

n = int(input("Enter number of elements: "))

a = []
for i in range(n):
    a.append(int(input(f"Enter element {i + 1}: ")))

freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

smallest = a[0]
for num in a:
    if num < smallest:
        smallest = num

print("Smallest value:", smallest)
print("Frequency:", freq[smallest])
