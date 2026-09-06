# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        node = head
        while node:
            nodes.append(node)
            node = node.next

        if len(nodes) == 1:
            return None

        n1, n2 = None, None
        node_to_remove_index = len(nodes) - n
        prev_node_index = node_to_remove_index - 1
        next_node_index = node_to_remove_index + 1

        if next_node_index < len(nodes):
            n2 = nodes[next_node_index]

        if prev_node_index >= 0:
            n1 = nodes[prev_node_index]
            n1.next = n2
        else:
            return n2

        return head
        