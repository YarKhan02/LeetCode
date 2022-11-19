def happy(n):
    while n != 1:
        p = 0
        if n < 7:
            return False

        n = str(n)
        
        for i in range(len(n)):
            p = p + int(n[i])*int(n[i])

        if p == 0:
            return False

        n = p

    return True

print(happy(19))