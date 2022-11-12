def remove():
    f = 1
    s = 1

    nums = [0,0,1,1,1,2,2,3,3,4]

    while f < len(nums):
        if nums[f] != nums[s - 1]:
            nums[s] = nums[f]
            s += 1

        f += 1

    return s

print(remove())