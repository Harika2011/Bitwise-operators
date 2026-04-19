def incDec(n):
    if n == 0:
        return
    print(n)        
    incDec(n - 1)    
    print(n)         

n = int(input("Enter a number: "))
print("Increasing-Decreasing sequence:⬆️⬇️")
incDec(n)
