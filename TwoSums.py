# SOLVE USING HASHMAP 

def two_sums():
    prev_map = {}
    target = 9
    arr = [2, 7, 11, 15]

    for i, n in enumerate(arr):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]

        prev_map[n] = i

print(two_sums())


# BRUTE FORCE ALGORITHM

# def two_sums():
#     target = 9
#     arr = [2, 7, 11, 15]
#     temp = []
#     i = 0
#     length = len(arr)
#     while(i < length):
#         j = i + 1
#         while(j < length):
#             if (arr[i] + arr[j]) == target:
#                 temp.append(i)
#                 temp.append(j)
#                 return temp

#             j += 1
        
#         j = 0
#         j = i + 1
#         i += 1

#     return None