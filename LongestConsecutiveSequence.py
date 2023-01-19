def lcs(nums):
    n = set(nums)
    count = 0

    for i in nums:
        if (i - 1) not in n:
            length = 0
            while (i + length) in n:
                length += 1

            count = max(count, length)

    return count

# n = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# n = [100, 4, 200, 1, 3, 2]
n = [0, 0]
print(lcs(n))