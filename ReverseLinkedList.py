def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None
    next = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev

    return head 