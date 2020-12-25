# Definition for a binary tree node.
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    import math
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1
        leftD=self.minDepth(root.left) if root.left else math.inf
        rightD=self.minDepth(root.right) if root.right else math.inf
        return 1 + min(leftD, rightD)
        