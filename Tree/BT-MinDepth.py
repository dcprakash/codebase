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
        leftD=self.minDepth(root.left) if root.left else float('inf')
        rightD=self.minDepth(root.right) if root.right else float('inf')
        return 1 + min(leftD, rightD)
        
    def easyMinDepth(self, root):
        return 1+min(self.easyMinDepth(root.left), self.easyMinDepth(root.right)) if root else 0
        
# Driver program to test above function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
s=Solution()
print(s.minDepth(root))
print(s.easyMinDepth(root))