def guess(k):
    n = 6
    if k == n:
        return 0
    elif k > n:
        return -1
    else:
        return 1

def guess_number(n):
    l, r = 0, n
    while n != 0:
        k = (l + r)//2
        pick = guess(k)
        if pick == 1:
            l = k + 1 
        elif pick == -1:
            r = k - 1
        elif pick == 0:
            return k

print(guess_number(10))