# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Example 1:
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# Example 2:
# Input: root1 = [1], root2 = [1]
# Output: true

# Example 3:
# Input: root1 = [1], root2 = [2]
# Output: false

# Example 4:
# Input: root1 = [1,2], root2 = [2,2]
# Output: true

# Example 5:
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false

# Constraints:
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

def leafSimilar(root1, root2):
    stack1 = [root1]
    stack2 = [root2]
    def is_leaf(node): return node.left is None and node.right is None

    while len(stack1) > 0:
        node1 = stack1.pop()
        node2 = stack2.pop()
        while not is_leaf(node1):
            if node1.left is not None: stack1.append(node1.left)
            if node1.right is not None: stack1.append(node1.right)
            node1 = stack1.pop()
        while not is_leaf(node2):
            if node2.left is not None: stack2.append(node2.left)
            if node2.right is not None: stack2.append(node2.right)
            node2 = stack2.pop()
        if node1.val is not node2.val: return False
    return True