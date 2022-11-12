def longest():
    s = 'bbbbbbbbb'

    output  = -1
    l = 0

    map = set()

    for i, n in enumerate(s):
        while n in map:
            map.remove(s[l])
            l += 1
        map.add(n)
        output = max(output, i - l + 1)
    
    return output

print(longest())

