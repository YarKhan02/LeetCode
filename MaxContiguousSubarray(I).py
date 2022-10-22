class Solution:
    def max_contiguous_subarray_sum(self, nums):
        max_so_far = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            print('i:', i)
            maximum = max(maximum + nums[i], nums[i])
            print('maximum:',maximum)
            max_so_far = max(maximum, max_so_far)
            print('max_so_far:', max_so_far)

        return max_so_far

max_sum = Solution()

print(max_sum.max_contiguous_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))