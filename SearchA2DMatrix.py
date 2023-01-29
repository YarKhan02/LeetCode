def search(matrix, target):
    low = i = 0
    high = len(matrix) - 1
    rows = len(matrix[0])

    while low <= high:
        mid = (low + high) // 2

        for i in range(rows):
            if matrix[mid][i] == target:
                return True
            
        if matrix[mid][i] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(search(matrix, target))