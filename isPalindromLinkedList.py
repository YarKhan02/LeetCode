def isPalindrome(self, head: Optional[ListNode]) -> bool:
    temp = head
    arr = []

    while temp != None:
        arr.append(temp.val)
        temp = temp.next

    n = len(arr) - 1

    for i in range(len(arr) - 1):
        if arr[i] != arr[n]:
            return False
        n -= 1

    return True