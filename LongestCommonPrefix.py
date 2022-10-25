def prefix():
    s = ["dog","racecar","car"]
    x = ''

    for _ in range(len(s[0])):
        for i in s:
            if _ == len(s) or i[_] != s[0][_]:
                return x

        x += s[0][_]

print(prefix())