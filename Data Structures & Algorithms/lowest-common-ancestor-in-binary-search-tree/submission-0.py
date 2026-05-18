# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        while current:
            # Both p and q are in left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left
            # Both p and q are in right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # Split: one on left, one on right, or current is p or q
            else:
                return current