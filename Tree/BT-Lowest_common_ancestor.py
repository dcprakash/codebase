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

class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None

			
def lca(root,p,q):
	if not root:	return None
	if root.data==p or root.data==q:	return root.data
	
	left=lca(root.left,p,q)
	right=lca(root.right,p,q)
	if left==None and right==None:	return None
	if left!=None and right!=None:	return root.data

	return left if left else right
    
        
        

# Driver program to test above function
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.right = Node(8)
print(lca(root,5,1))
        
'''
        3
	5		1
  6   2	      8
'''