def test_location(mid_index, target):
    start = 0
    end = len(nums) - 1

    if mid_index >= 0 and nums[mid_index] == target:
        return 'Found'

    elif nums[mid_index] <= nums[end]:
        if nums[mid_index] >= target and target <= nums[end]:
            return 'Left'
        elif nums[mid_index] <= target and target >= nums[start]:
            return 'Left'
        else:
            return 'Right'

    else:
        if nums[mid_index] >= target and target <= nums[end]:
            return 'Right'
        elif nums[mid_index] <= target and target >= nums[start]:
            return 'Right'
        else:
            return 'Left'

def small_test(mid_index, target):
    start = 0
    end = len(nums) - 1

    if mid_index >= 0 and nums[mid_index] == target:
        return 'Found'

    elif nums[mid_index] <= nums[end]:
        if nums[mid_index] <= target and target >= nums[start]:
            return 'Right'
        else:
            return 'Left'

    else:
        if nums[mid_index] >= target and target <= nums[start]:
            return 'Right'
        else:
            return 'Left'

def count_rotation(nums, target):
    low = 0
    high = len(nums) - 1

    if high <= 2 and nums[low] < nums[high]:
        while low <= high:
            mid_index = (low + high)//2

            result = small_test(mid_index, target)

            if result == 'Found':
                return mid_index
            elif result == 'Left':
                high = mid_index - 1
            else:
                low = mid_index + 1

    if nums[low] < nums[high] and high > 2:
        while low <= high:
            mid_index = (low + high)//2

            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                low = mid_index + 1
            else:
                high = mid_index - 1
    else:
        while low <= high:
            mid_index = (low + high)//2

            result = test_location(mid_index, target)

            if result == 'Found':
                return mid_index
            elif result == 'Left':
                high = mid_index - 1
            else:
                low = mid_index + 1

    return -1


nums = [1]
target = 5
print(count_rotation(nums, target))