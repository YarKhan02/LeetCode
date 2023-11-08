class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None

    if root == p or root == q:
        return root
    
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root
    else:
        return l or r

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)

    return node

def display_keys(node, space = '\t', level = 0):
    global count
    if node is None:
        print(space * level + '')
        return

    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    display_keys(node.left, space, level + 1)

    print(space * level + str(node.key))

    display_keys(node.right, space, level + 1)

    return ''

tree = parse_tuple((((None, 4, (13, 7, (None, 12, None))), 1, (8, 3, 9)), 0, ((10, 5, (15, 11, 14)), 2, (None, 6, None))))
lca = lowestCommonAncestor(tree, 13, 9)
print(display_keys(tree, '   '))
print('Lowest Common Ancestor: {}'.format(lca))