def duplicates(n):
    hash_map = {}

    for i, n in enumerate(n):
        if n in hash_map:
            return True
        hash_map[n] = i

    return False

print(duplicates([1,2,3,4]))