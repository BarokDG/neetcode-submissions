# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([p, q])
        while q:
            n1 = q.popleft()
            n2 = q.popleft()

            if not n1 and not n2:
                continue

            if bool(n1) != bool(n2) or n1.val != n2.val:
                return False
            
            q.append(n1.left)
            q.append(n2.left)

            q.append(n1.right)
            q.append(n2.right)
        
        return True