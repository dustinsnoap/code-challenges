// Reverse a singly linked list.

// Example:
// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?

const reverseList = head => {
    let prev_node = null
    let current_node = head
    while(current_node) {
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    }
    return prev_node
}