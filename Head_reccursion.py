def printNumbers(n):
    if n == 0:
        return
    printNumbers(n - 1)  
    print(n)

n = int(input("Enter a number: "))
print("Numbers from 1 to", n, "using head recursion:")
printNumbers(n)
