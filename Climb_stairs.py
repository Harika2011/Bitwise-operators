def countWays(n):
    if n == 0:
        return 1  
    elif n < 0:
        return 0  
    
    return countWays(n-1) + countWays(n-2) + countWays(n-3)

stairs = int(input("Enter number of stairs: "))
ways = countWays(stairs)
print("Number of ways to climb", stairs, "stairs:", ways)
