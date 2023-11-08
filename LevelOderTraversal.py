def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        level_nodes = []
        level_size = len(queue)

        for _ in range(level_size):
            current = queue.popleft()
            level_nodes.append(current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        result.append(level_nodes)

    return result