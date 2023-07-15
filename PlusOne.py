def plus_one(digits):
    s = ''

    for i in digits:
        s += str(i)

    n = int(s)

    s = str(n + 1)

    result = []

    for i in s:
        result.append(int(i))

    return result

digits = [1, 2, 3]

print(plus_one(digits))