# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# SETUP
from tools import LinkedList

# CODE

def reverseList(head):
    prev_node = None
    current = head
    while(current):
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
    return prev_node

def reverseList2(head):
    prev_node = None
    current = head
    while(current):
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
    return prev_node

def reverseListRecursive(head):
    if head is None or head.next is None: return head
    tmp = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return tmp


# TESTING
tester = LinkedList()

print('TEST 1')
input = [1,2,3,4,5]
tester.test(reverseList, input)

print('TEST 2')
input = [1,2,3,4,5]
tester.test(reverseList2, input)

print('TEST 3')
input = [1,2,3,4,5]
tester.test(reverseListRecursive, input)