def generate(n):
    stack = []
    output = []

    def backtrack(openN, closeN):
        if closeN == openN == n:
            output.append("".join(stack))
            return

        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(')')
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)

    return output

n = 3
print(generate(n))