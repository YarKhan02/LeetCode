def product(n):
    sign = 1
    for i in range(len(n)):
        sign = sign * n[i]

    if sign == 0:
        return 0
    elif sign > 0:
        return 1
    else:
        return -1 

print(product([-1, -2, -3, -4, 3, 2, 1]))