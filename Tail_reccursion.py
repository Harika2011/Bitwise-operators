def printNumbers(n):
    if n == 0:
        return
    print(n)
    printNumbers(n - 1) 
    
n = int(input("Enter a number: "))
print("Numbers from", n, "to 1 using tail recursion:")
printNumbers(n)
