# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def dfs(node, depth):
            if not node:
                return

            if len(levels) == depth:
                levels.append([])
            
            levels[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)

        out = []

        for level in levels:
            out.append(level[-1])

        return out



