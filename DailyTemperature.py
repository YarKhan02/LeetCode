def daily(temperatures):
    output = [0] * len(temperatures)
    stack = []

    for i, n in enumerate(temperatures):
        while stack and n > stack[-1][0]:
            stackT, stackInd = stack.pop()
            output[stackInd] = i - stackInd
        stack.append([n, i])
    return output

temp = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily(temp))