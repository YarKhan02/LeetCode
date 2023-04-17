def find_min(nums):
    output = nums[0]
    low = 0
    high = len(nums) - 1

    while low <= high:
        if nums[low] < nums[high]:
            output = min(output, nums[low])
            break

        midIndex = (low + high) // 2
        output = min(output, nums[midIndex])

        if nums[midIndex] >= nums[low]:
            low = midIndex + 1
        else:
            high = midIndex - 1

    return output

# nums = [3, 4, 5, 1, 2]
nums = [4, 5, 6, 7, 0, 1, 2]
print(find_min(nums))