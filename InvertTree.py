def invertTree(root):
    if (root == None):
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root