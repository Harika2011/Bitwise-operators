def get_combinations(digits, mapping, index, path, result):
    if index == len(digits):
        result.append("".join(path))
        return
    for char in mapping[digits[index]]:
        path.append(char)
        get_combinations(digits, mapping, index + 1, path, result)
        path.pop()

def phone_keypad_combinations(digits):
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    result = []
    if digits:
        get_combinations(digits, mapping, 0, [], result)
    return result

digits = "234"
combinations = phone_keypad_combinations(digits)
for combo in combinations:
    print(combo)
