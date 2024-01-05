def jump_game(nums):
    step = 0

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= step:
            step = i
        
    return True if step == 0 else False

nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
print(jump_game(nums))