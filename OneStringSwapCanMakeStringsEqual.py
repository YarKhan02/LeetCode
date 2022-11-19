def swap(s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) != sorted(s2):
        return False

    x = []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            x.append(i)

    if len(x) == 0 or len(x) == 2:
        return True

    return False



print(swap("attack", "defend")) 
