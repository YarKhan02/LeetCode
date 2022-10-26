def valid():
    s = '([])'
    stack = []
    closeToOpen = { ")": "(",
                    "]": "[",
                    "}": "{"
                }

    for i in s:
        if i in closeToOpen:
            if stack[-1] == closeToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return True if not stack else False

print(valid())