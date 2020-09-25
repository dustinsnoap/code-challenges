# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

def maxDepth(root):
    if root is None: return 0
    stack = [root]
    root.val = 1
    max_depth = 1
    while len(stack) > 0:
        root = stack.pop()
        if root.left:
            root.left.val = root.val + 1
            stack.append(root.left)
        if root.right:
            root.right.val = root.val + 1
            stack.append(root.right)
        max_depth = max(root.val, max_depth)
    return max_depth

def maxDepthRecursive(root):
    if not root: return 0
    left = maxDepth(root.left) + 1
    right = maxDepth(root.right) + 1
    return max(left, right)