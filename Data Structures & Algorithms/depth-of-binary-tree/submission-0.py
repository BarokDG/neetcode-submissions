# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        rdepth, ldepth = 1, 1

        if root.left:
            ldepth += self.maxDepth(root.left)
        
        if root.right:
            rdepth += self.maxDepth(root.right)

        return max(ldepth, rdepth)