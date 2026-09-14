# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        carry = 0
        curr = res
        while l1 or l2 or carry:
            val = carry if carry else 0

            if l1:
                val += l1.val
                l1 = l1.next
            
            if l2:
                val += l2.val
                l2 = l2.next

            carry = val // 10
            val %= 10
            
            curr.next = ListNode(val)
            curr = curr.next

        return res.next