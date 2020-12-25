"""
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/3024/
https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lca(self, root, p, q):
        if root==None:
            return None

        if root==p or root==q:
            return root
        
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        
        if left==None and right==None:
            return None
        
        if left!=None and right!=None:
            return root
        
        return left if left else right
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p, q)
        
