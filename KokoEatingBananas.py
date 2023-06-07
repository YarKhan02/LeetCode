def koko(piles, h):
    max_n = max(piles)
    hour = 0
    prev_hour = 999999999999
    output = 999999999999

    l = 1
    r = max_n

    while l <= r:
        i = 0
        k = (l + r) // 2
        # print('k - ', k)

        while i < len(piles):
            if (piles[i] % k) == 0:
                hour += (piles[i] // k)
                # print(piles[i] // k)
            else:
                hour += (piles[i] // k) + 1
                # print((piles[i] // k) + 1)
            i += 1

        prev_hour = min(prev_hour, hour)

        # print('hour - ', hour)
        # print('prev_hour - ', prev_hour)

        if hour > h:
            l = k + 1
            hour = 0
        else:
            r = k - 1

            if prev_hour <= hour:
                output = min(output, k)
                hour = 0

    return output

piles = [3, 6, 7, 11]
piles = [30, 11, 23, 4, 20]
piles = [30, 11, 23, 4, 20]
h = 8

print(koko(piles, 6))