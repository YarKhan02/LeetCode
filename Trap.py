def trap(height):
    if not height: return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    output = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            output += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            output += rightMax - height[r]

    return output

nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(nums))