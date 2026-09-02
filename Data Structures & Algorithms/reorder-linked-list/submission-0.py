# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        l, r = 1, len(nodes) - 1
        while l <= r:
            n2 = nodes[r]
            n1 = nodes[l]

            head.next = n2
            head.next.next = n1

            head = head.next.next

            l += 1
            r -= 1
        
        head.next = None