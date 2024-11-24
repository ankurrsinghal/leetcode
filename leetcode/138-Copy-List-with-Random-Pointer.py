"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        new_head = None
        while curr:
            if not new_head:
                new_head = curr.next

            next_node_to_itr = None
            if curr.next.next:
                next_node_to_itr = curr.next.next
                curr.next.next = curr.next.next.next
            else:
                curr.next.next = None

            curr = next_node_to_itr
        
        return new_head