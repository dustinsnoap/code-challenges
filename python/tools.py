class LinkedList:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def create_linked_list(self, arr):
        root = self.ListNode(arr.pop(0))
        prev_node = root
        for n in arr:
            node = self.ListNode(n)
            prev_node.next = node
            prev_node = node
        return root
    def copy_linked_list(self, head):
        if head is None: return head
        new_node = self.ListNode(head.val)
        new_node.next = self.copy_linked_list(head.next)
        return new_node
    def print_list(self, head):
        print(head.val, end='')
        head = head.next
        while head:
            print(' >', head.val, end='')
            head = head.next
        print()

    def test(self, fnc, input):
        llcoollist = self.create_linked_list(input)
        print('input:    ', end='')
        self.print_list(llcoollist)
        newlist = fnc(llcoollist)
        print('output:   ', end='')
        self.print_list(newlist)