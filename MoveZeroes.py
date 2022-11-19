def zeroes(nums):
    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

    return nums

print(zeroes([0, 1, 0, 3, 12]))