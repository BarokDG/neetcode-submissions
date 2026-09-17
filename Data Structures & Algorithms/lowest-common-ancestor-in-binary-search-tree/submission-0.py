# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = self.getAncestors(root, p)
        q_ancestors = self.getAncestors(root, q)

        least_common_ancestor = root
        
        min_ancestors = min(len(p_ancestors), len(q_ancestors))
        for i in range(min_ancestors):
            if p_ancestors[i].val == q_ancestors[i].val:
                least_common_ancestor = p_ancestors[i]

        return least_common_ancestor
    
    def getAncestors(self, root: TreeNode, node: TreeNode) -> list:
        ancestors = [root]

        curr = root
        while curr.val != node.val:
            if curr.val > node.val:
                curr = curr.left
            else:
                curr = curr.right

            ancestors.append(curr)

        return ancestors

        