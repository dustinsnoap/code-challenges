// Reverse a singly linked list.

// Example:
// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?

package main

func reverseList(head *ListNode) *ListNode {
	var prev_node *ListNode
	for head != nil {
		next_node := head.Next
		head.Next = prev_node
		prev_node = head
		head = next_node
	}
	return prev_node
}