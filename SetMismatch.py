def mismatch(nums):
    output = 0
    result = []

    l = len(nums) - 1

    for i in range(l):
        if nums[i] == nums[i + 1]:
            output = nums[i]
            if i + 1 == len(nums) - 1:
                result.append(output)
                if output - 1 != 0: 
                    result.append(output - 1)
                else:
                    result.append(output + 1)
                break
            else:
                result.append(output)
                result.append(output + 1)
                break

    return result

nums = [1, 2, 2, 4]
# nums = [1, 1]
print((mismatch(nums)))