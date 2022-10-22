
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums: 
            return None

        mid = len(nums) // 2

        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid + 1:])

        return head

solution = Solution()

print(solution.sortedArrayToBST([-10,-3,0,5,9]))