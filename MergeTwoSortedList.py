# TWO SORTED ARRAY LIST SOLUTION

def merge(num1, num2):
    merged = []
    i = 0
    j = 0

    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i += 1
        else:
            merged.append(num2[j])
            j += 1

    return merged + num1[i:] + num2[j:]

print(merge([1, 4, 3, 9, 11], [-1, 0, 2, 3, 8, 12]))


# LINKED LIST SOLUTION

class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

class Solution:
        def merge(self, list1, list2):
                dummy = ListNode()
                tail = dummy

                while list1 and list2:

                        if list1.val < list2.val:
                                tail.next = list1
                                list1 = list1.next
                        else:
                                tail.next = list2
                                list2 = list2.next
                        
                        tail = tail.next
                        
                if list1:
                        tail.next = list1
                elif list2:
                        tail.next = list2

                return dummy.next