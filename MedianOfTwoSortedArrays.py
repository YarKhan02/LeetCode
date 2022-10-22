def merge(nums1, nums2):
    merged = []

    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    list = merged + nums1[i:] + nums2[j:]
    length = len(list) - 1
    print('length:', length)

    if length <= 2:
        return list
    elif length % 2 == 0:
        median = length // 2
        return float(list[median])
    else:
        median = length // 2
        result = (list[median] + list[median + 1]) / 2
        return result


print(merge([1, 7], []))


[-1, 0, 1, 2, 3, 4, 7, 8, 9, 11, 12, 16]