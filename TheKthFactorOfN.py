def KthFactor(n, k):
    factor = []

    y = n

    for i in range(1, y + 1):
        if n % i == 0:
            factor.append(i)

    if k > len(factor): return -1
    else: return factor[k - 1]

print(KthFactor(12, 3))