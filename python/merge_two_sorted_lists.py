# Merge two sorted linked lists and return it as a new sorted list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

def mergeTwoLists(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    l2.next = mergeTwoLists(l1, l2.next)
    return l2