def palindrome(n):
    n = str(n) 
    length = len(n)

    if length < 2:
        return True

    if n[0] == n[length - 1]:
        return palindrome(n[1: length - 1])

    return False



print(palindrome(10))