def merge():
    n1 = [2, 0]
    n2 = [1]

    n = 1
    m = 1
    end = m + n - 1

    while m > 0 and n > 0:

        if n1[n - 1] > n2[m - 1]:
            n1[end] = n1[n - 1] 
            n -= 1
        else:
            n1[end] = n2[m - 1]
            m -= 1

        end -= 1

    while m > 0:
        n1[end] = n2[m - 1]
        end -= 1
        m -= 1

    return n1

print(merge())