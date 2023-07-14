def counting_bits(n):
    output = [0] * (n + 1)

    for i in range(n + 1):
        output[i] = output[i >> 1] + (i & 1)

    return output 

n = 5

print(counting_bits(n))