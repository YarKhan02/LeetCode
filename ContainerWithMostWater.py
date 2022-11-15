def water():
    height = [1,8,6,2,5,4,8,3,7]
    l = 0
    r = len(height) - 1
    output = 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        output = max(output, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return output


print(water())