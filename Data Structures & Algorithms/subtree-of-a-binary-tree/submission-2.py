# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False

            if self.isSameTree(node, subRoot):
                return True
                
            return dfs(node.left) or dfs(node.right)           
        
        return dfs(root)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if not n1 and not n2:
                return True
                
            if n1 and n2 and n1.val == n2.val:
                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
            
            return False
        
        return dfs(p, q)

            