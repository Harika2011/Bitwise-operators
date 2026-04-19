def takeInput():
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        print("Negative number entered. Stopping...🛑")
        return
    takeInput()  

takeInput()
