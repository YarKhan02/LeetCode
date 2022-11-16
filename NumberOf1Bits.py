def bits():
    r = 0
    while n:
        n = n & (n - 1)
        r += 1

    return r

print(bits())