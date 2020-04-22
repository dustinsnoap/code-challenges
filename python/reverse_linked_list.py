# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

def reverseList(head):
    prev_node = None
    current = head
    while(current):
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
    return prev_node