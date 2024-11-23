# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if size == 1:
            return None

        pointer = 0
        last = None
        curr = head
        pos = size - n
        while pointer < pos:
            pointer += 1
            last = curr
            curr = curr.next
        
        if last == None:
            head = head.next
        else:
            last.next = curr.next

        return head