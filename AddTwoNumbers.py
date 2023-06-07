def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0

            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            n = val1 + val2 + carry
            carry = n // 10
            x = n % 10
 
            if head == None:
                head = ListNode(x)
            else:
                newNode = ListNode(x)
                current = head

                while current.next != None:
                    current = current.next

                current.next = newNode

        return head