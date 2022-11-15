def position(nums, target):
    left = binary_search(nums, target, True)
    right = binary_search(nums, target, False)

    return left, right

def binary_search(nums, target, direction):
    low = 0
    high = len(nums) - 1
    i = -1

    while low <= high:
        mid_index = (low + high)//2

        if nums[mid_index] > target:
            high = mid_index - 1
        elif nums[mid_index] < target:
            low = mid_index + 1
        else:
            i = mid_index
            if direction:
                high = mid_index - 1
            else:
                low = mid_index + 1

    return i


nums = [1, 2, 2 ,2 ,3 ,4 ,5]
target = 2

print(position(nums, target)) 