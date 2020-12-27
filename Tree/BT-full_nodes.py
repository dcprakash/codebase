"""
Your module description
"""

# Recursive Python program for DFS traversal of Binary Tree

# A node structure
# https://www.geeksforgeeks.org/count-full-nodes-binary-tree-iterative-recursive/

class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None

			
def fullnodes(root):
    if not root:
        return 0
    global res
    if root.left and root.right:
        res.append(root.data)
    if root.left: fullnodes(root.left)
    if root.right: fullnodes(root.right)
    return res
    



# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
res = []
print(fullnodes(root))
