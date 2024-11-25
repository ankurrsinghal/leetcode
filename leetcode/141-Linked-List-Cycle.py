# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()

        curr = head
        while curr:
            node_set.add(curr)
            curr = curr.next
            if curr in node_set:
                return True
        
        return False