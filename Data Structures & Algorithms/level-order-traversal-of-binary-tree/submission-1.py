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
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    temp_out.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if temp_out:
                out.append(temp_out)

        return out