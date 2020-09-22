class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isPowerOfTwo(n):
    return (n and (not(n & (n - 1)))) 

def view_tree(root):
    stack = [root]
    count = 1
    while len(stack) > 0:
        count += 1
        node = stack.pop(0)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
        print(f'{node.value} ', end='')
        if isPowerOfTwo(count): print()

def build_tree(arr):
    root = Node(arr.pop(0))
    queue = [root]
    while len(arr) > 0:
        node = queue.pop(0)
        node.left = Node(arr.pop(0))
        node.right = Node(arr.pop(0))
        if node.left.value: queue.append(node.left)
        if node.right.value: queue.append(node.right)
    return root