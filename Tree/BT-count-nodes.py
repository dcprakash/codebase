"""
https://leetcode.com/problems/count-complete-tree-nodes/submissions/
"""

# Recursive Python program for DFS traversal of Binary Tree

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None

	
def countNodes(root):
    return 1 + countNodes(root.left) + countNodes(root.right) if root else 0
    

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(countNodes(root))
