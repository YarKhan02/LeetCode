def preorder(root: 'Node'):
    def dfs(root, output):
        if not root:
            return None
        output.append(root.val)
        for child in root.children:
            dfs(child, output)
        return output
        
    return dfs(root, [])

print(preorder([1,None,3,2,4,None,5,6]))