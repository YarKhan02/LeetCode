def square(A):
    for i in range(len(A)):
        A[i] = A[i]*A[i]

    return sorted(A)

print(square([-4, -1, 0, 3, 10]))