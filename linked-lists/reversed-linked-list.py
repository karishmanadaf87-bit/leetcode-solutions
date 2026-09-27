class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous


def create_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def display(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


# Test Case 1 - Typical case
head1 = create_list([1, 2, 3, 4, 5])
result1 = Solution().reverseList(head1)
print("Test Case 1:", display(result1))

# Test Case 2 - Edge case
head2 = create_list([])
result2 = Solution().reverseList(head2)
print("Test Case 2:", display(result2))