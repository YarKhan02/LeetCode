def max_profit(nums):
    profit = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            profit += (nums[i] - nums[i - 1])

    return profit


print(max_profit([7, 6, 4, 3, 1]))