def dfs(node):
        if not node:
            return 0

        l = dfs(node.left)
        r = dfs(node.right)
            
        self.diameter = max(self.diameter, l + r)

        return 1 + max(l, r)

    self.diameter = 0
    dfs(root)
    return self.diameter 