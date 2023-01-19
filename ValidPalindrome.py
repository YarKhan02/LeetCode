def palindrome(s):
    x = ''

    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
            if (ord(i) >= 65 and ord(i) <= 90):
                i = ord(i) + 32
                i = chr(i)
            x = x + i

    l = 0
    r = len(x) - 1

    while l <= r:
        if x[l] == x[r]:
            l += 1
            r -= 1
        else:
            return False

    return True


# s = 'A man, a plan, a canal: Panama'
# s = 'race a car'
# s = ''
s = '0P'
print(palindrome(s))