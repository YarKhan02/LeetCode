def perimeter(A):
    A = sorted(A)

    for i in range(len(A) - 3, -1, -1):
        if A[i] + A[i + 1] > A[i + 2]:
            return A[i] + A[i + 1] + A[i + 2]
        
    return 0

print(perimeter([2, 1, 1]))