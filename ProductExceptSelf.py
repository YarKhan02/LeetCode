def except_self(n):
    arr = [1] * len(n)
    pre = 1
    
    for i in range(len(n)):
        arr[i] = pre
        pre *= n[i]

    post = 1

    for i in range(len(n) - 1, -1, -1):
        arr[i] *= post
        post *= n[i]

    return arr

n = [1, 2, 3, 4]
print(except_self(n))