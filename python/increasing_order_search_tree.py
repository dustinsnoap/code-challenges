# Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \ 
# 1        7   9

# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9  

# Constraints:
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.

from trees import build_tree, view_tree, Node

def increasingBST(root):
    sorted_arr = []
    def inorder(node):
        if node:
            inorder(node.left)
            sorted_arr.append(node.value)
            inorder(node.right)
    inorder(root)

    root = Node(sorted_arr.pop(0))
    current_node = root
    for n in sorted_arr:
        current_node.right = Node(n)
        current_node = current_node.right

    return root


input = [5,3,6,2,4,None,8,1,None,None,None,7,9]
output = increasingBST(build_tree(input))

view_tree(output)
