from collections import defaultdict

def grp_anagram(s):
    hash_map = defaultdict(list)

    for i in s:
        count = [0] * 26
        for c in i:
            count[ord(c) - ord('a')] += 1

        hash_map[tuple(count)].append(i)

    return hash_map.values()

s = ["eat","tea","tan","ate","nat","bat"]
print(grp_anagram(s))