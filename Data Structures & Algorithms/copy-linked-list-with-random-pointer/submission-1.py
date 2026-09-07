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
            return None
            
        new_head = Node(head.val)

        curr = head
        new_curr = new_head
        mp = {}
        while curr:
            mp[curr] = new_curr

            curr = curr.next
            if curr:
                new_curr.next = Node(curr.val)
                new_curr = new_curr.next
        
        curr = head
        new_curr = new_head
        while curr:
            new_curr.random = mp[curr.random] if curr.random else None

            curr = curr.next
            new_curr = new_curr.next
        
        return new_head
