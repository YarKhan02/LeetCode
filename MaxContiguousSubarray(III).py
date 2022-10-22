class Solution:
    def max_contiguous_subarray_sum(self, nums):
        n = len(nums)
        max_sum = -10000

        for left in range(0, n):
            print('\nleft:', left)

            for right in range(left, n):
                print('right:',right)

                window_sum = 0
                print('window_sum:', window_sum)

                for k in range(left, right + 1):
                    print('k:', k, 'nums[k]', nums[k])

                    window_sum += nums[k]
                    print('window_sum_k:', window_sum)

                max_sum = max(max_sum, window_sum)

        return max_sum

max_sum = Solution()

print(max_sum.max_contiguous_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))