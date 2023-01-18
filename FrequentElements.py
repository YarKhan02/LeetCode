def frequent(nums, k):
    n = nums
    hash_map = {}
    freq = [[] for _ in range(len(n))]

    for i in n:
        hash_map[i] = hash_map.get(i, 0) + 1

    for j, c in hash_map.items():
        freq[c].append(j)

    result = []

    for k in range(len(freq) -1, 0, -1):
        for z in freq[k]:
            result.append(z)
            if len(result) == k:
                return result                

n = [1, 1, 1, 2, 2, 3]
print(frequent(n, 2))