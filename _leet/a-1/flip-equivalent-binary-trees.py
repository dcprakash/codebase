'''
https://leetcode.com/problems/flip-equivalent-binary-trees/solution/

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is root2:  return True     # check if both point to same tree if not root1 or not root2:  return root1 == root2
        if not root1 or not root2 or root1.val != root2.val:
            return False

        # first condition is required, when both root1 and root2 point to same tree
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))