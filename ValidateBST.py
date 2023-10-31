class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, minimum, maximum):
            if (node == None):
                return True

            if (node.val <= minimum) or (node.val >= maximum):
                return False

            left = valid(node.left, minimum, node.val)
            if (left):
                right = valid(node.right, node.val, maximum)
                return right

            return False

        return valid(root, -(sys.maxsize), sys.maxsize)