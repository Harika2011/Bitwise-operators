def generateParentheses(n):
    def backtrack(open_count, close_count, current, result):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(open_count + 1, close_count, current + "(", result)

        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ")", result)

    result = []
    backtrack(0, 0, "", result)
    return result

n = int(input("Enter number of parentheses pairs: "))
combinations = generateParentheses(n)

print("Balanced Parentheses Combinations:")
for combo in combinations:
    print(combo)
