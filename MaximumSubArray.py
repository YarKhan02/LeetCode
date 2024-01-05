def maximum_sub_array(arr):
    maximum_sum = arr[0]
    current_sum = 0

    for n in arr:
        if current_sum < 0:
            current_sum = 0

        current_sum += n
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum
    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maximum_sub_array(arr))