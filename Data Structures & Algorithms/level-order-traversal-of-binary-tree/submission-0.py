# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        out = []

        q = deque([root])
        while q:
            temp_out = []
            next_q = deque()
            while q:
                node = q.popleft()
                temp_out.append(node.val)

                if node.left:
                    next_q.append(node.left)
                
                if node.right:
                    next_q.append(node.right)
        
            out.append(temp_out)
            q = next_q

        return out