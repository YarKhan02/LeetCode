def anagram(s, t):
    if len(s) != len(t):
        return False

    hash_map1 = {}
    hash_map2 = {}

    for i, n in enumerate(s):
        if n in hash_map1:
            hash_map1[n] = hash_map1.get(n) + 1
        else:
            hash_map1[n] = 1

    for i, n in enumerate(t):
        if n in hash_map2:
            hash_map2[n] = hash_map2.get(n) + 1
        else:
            hash_map2[n] = 1

    if len(hash_map1) == len(hash_map2):
        for i, n in enumerate(s):
            if n not in hash_map2:
                return False
            elif hash_map1.get(n) != hash_map2.get(n):
                return False
    else:
        return False

    return True

s = 'aacc'
t = 'ccac'

print(anagram(s, t))