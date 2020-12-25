"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    import math
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1
        leftD=self.maxDepth(root.left) if root.left else -math.inf
        rightD=self.maxDepth(root.right) if root.right else -math.inf
        return 1 + max(leftD, rightD)
        