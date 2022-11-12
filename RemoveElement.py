def remove():
    f = 0
    i = 0

    nums = [0,1,2,2,3,0,4,2]
    # nums = [3, 2, 2, 3]

    while f < len(nums):
        if nums[f] != 2:
            nums[i] = nums[f]
            i += 1

        f += 1

    return i

print(remove())