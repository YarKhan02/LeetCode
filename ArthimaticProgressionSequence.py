def sequnce(arr):
    arr = sorted(arr)
    diff = 0
    final = []

    for i in range(len(arr) - 1):
        diff = arr[i] - arr[i + 1]
        final.append(diff)
        if diff != final[0]:
            return False

    return True

print(sequnce([1, 5, 3]))