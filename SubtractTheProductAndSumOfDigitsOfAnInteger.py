def sps(n):
    p = 1
    s = 0
    while n >= 1:
        r = n % 10
        n = n // 10
        p *= r
        s += r

    sub = p - s

    return sub

print(sps(1))