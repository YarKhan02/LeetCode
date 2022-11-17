def nearest(x, y, nums):
    best = 10 ** 10
    index = -1

    for i, (x1, y1) in enumerate(nums):
        if x == x1 or y == y1:
            dist = abs(x - x1) + abs(y - y1)

            if dist < best:
                index = i
                best = dist

    return index

print(nearest(3, 4, [[1,2], [3,1], [2,4], [2,3], [4,4]]))