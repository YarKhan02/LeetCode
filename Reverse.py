def reverse():
    x = -123
    s = str(x)
    n = ''


    for i in range(len(s) - 1, -1, -1):
        if (ord(s[i]) < 48) or (ord(s[i]) > 57):
            n = s[i] + n
        else:
            n = n + s[i]

    if int(n) > pow(2, 31) - 1 or int(n) < pow(-2, 31):
        return 0

    return int(n)


print(reverse())    