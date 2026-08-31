# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = ListNode(head.val)

        curr = head
        while curr.next:
            curr = curr.next

            new_node = ListNode(curr.val, new_head)
            new_head = new_node
        
        return new_head