# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3
#         [1,2,3],   [1,2,3]
# Output: true

# Example 2:
# Input:     1         1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# Output: false

# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# Output: false

def isSameTree(p, q):
    if p and not q: return False
    if q and not p: return False
    if not p and not q: return True
    
    stack_1 = [p]
    stack_2 = [q]

    while len(stack_1) > 0:
        node1 = stack_1.pop()
        node2 = stack_2.pop()
        if node1.val != node2.val: return False
        if node1.left and not node2.left: return False
        if node2.left and not node1.left: return False
        if node1.right and not node2.right: return False
        if node2.right and not node1.right: return False
        if node1.left and node2.left:
            stack_1.append(node1.left)
            stack_2.append(node2.left)
        if node1.right and node2:
            stack_1.append(node1.right)
            stack_2.append(node2.right)
            
    return True