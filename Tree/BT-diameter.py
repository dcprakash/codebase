"""
https://leetcode.com/problems/diameter-of-binary-tree/

"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    import math
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=1
        
        def helper(node):
            if not node:
                return 0
            L=helper(node.left)
            R=helper(node.right)
            self.ans=max(self.ans, L+R+1)
            return max(L,R)+1
            
        helper(root)
        return self.ans-1
        