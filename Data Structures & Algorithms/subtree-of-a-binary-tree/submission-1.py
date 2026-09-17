# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False

            if self.compare(node, subRoot):
                return True
                
            return dfs(node.left) or dfs(node.right)           
        
        return dfs(root)
    
    def compare(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        q1 = deque([tree1])
        q2 = deque([tree2])

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            if n1.val != n2.val:
                return False
            
            if n1.left:
                q1.append(n1.left)
            
            if n1.right:
                q1.append(n1.right)

            if n2.left:
                q2.append(n2.left)
            
            if n2.right:
                q2.append(n2.right)
        
        return len(q1) == len(q2)

            