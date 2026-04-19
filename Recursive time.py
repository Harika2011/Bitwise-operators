def func1(n):
    if n == 0:
        print("func1 reached base case.")
        return
    print(f"func1 called with n = {n}")
    func1(n - 1)

def func2(n):
    if n == 0:
        print("func2 reached base case.")
        return
    print(f"func2 called with n = {n}")
    func2(n - 1)
    func2(n - 1)

print("Testing func1 (Linear Recursion):")
func1(5)

print("\nTesting func2 (Exponential Recursion):")
func2(3)
