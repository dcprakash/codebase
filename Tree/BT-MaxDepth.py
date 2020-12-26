"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/


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
        
"""
"""
Your module description
"""

# Recursive Python program for level 
# order traversal of Binary Tree

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None


import math
def maxdepth(root):
	if not root:
		return 0
	if root.left is None and root.right==None:
		return 1
	ld=maxdepth(root.left) if root.left else -math.inf
	rd=maxdepth(root.right) if root.right else -math.inf
	return max(ld,rd)+1
        
        

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print(maxdepth(root))
